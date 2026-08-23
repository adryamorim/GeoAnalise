import os
from pathlib import Path
import glob
import pandas as pd
import geopandas as gpd

# ==============================================================================
# 1. CONFIGURAÇÕES DE CAMINHOS (AJUSTE CONFORME SUA MÁQUINA)
# ==============================================================================
DIRETORIO_PROJETO = r"C:\Geo\Escola de Governo"
# Nome do arquivo GeoJSON de glebas corrigido pelo usuário
CAMINHO_GEOJSON_GLEBAS = os.path.join(DIRETORIO_PROJETO, "Mesclados.geojson") 
CAMINHO_SAIDA_CSV = os.path.join(DIRETORIO_PROJETO, "Fomento_Municipal_ISVT.csv")

# ==============================================================================
# 2. PROCESSAMENTO E CONCATENAÇÃO DAS OPERAÇÕES (2016 A 2026)
# ==============================================================================
print("1/5. Buscando arquivos locais de operações de 2016 a 2026...")

# Busca todos os arquivos que começam com 'SICOR_OPERACAO_BASICA_ESTADO_' na pasta
padrao_arquivos = os.path.join(DIRETORIO_PROJETO, "SICOR_OPERACAO_BASICA_ESTADO_*.csv")
arquivos_operacoes = glob.glob(padrao_arquivos)

if not arquivos_operacoes:
    raise FileNotFoundError(f"Nenhum arquivo correspondente a {padrao_arquivos} foi encontrado na pasta.")

print(f"Encontrados {len(arquivos_operacoes)} arquivos de operações para processar.")

dfs_operacoes = []
for caminho_csv in arquivos_operacoes:
    ano = os.path.basename(caminho_csv).split('_')[-1].replace('.csv', '')
    print(f" -> Lendo ano {ano}...")
    
    # Tratando codificações diferentes comuns nos arquivos do Banco Central
    try:
        df_ano = pd.read_csv(caminho_csv, sep=';', encoding='utf-8', low_memory=False)
    except UnicodeDecodeError:
        df_ano = pd.read_csv(caminho_csv, sep=';', encoding='latin1', low_memory=False)
    
    # ==============================================================================
    # MAPEAMENTO CORRIGIDO COM BASE NA ESTRUTURA REAL DO SEU CSV
    # ==============================================================================
    # 1. O id_referencia_bacen no seu CSV veio com o caractere '#' no início: '#REF_BACEN'
    col_bacen = '#REF_BACEN'
    # 2. O nu_ordem veio em maiúsculo: 'NU_ORDEM'
    col_ordem = 'NU_ORDEM'
    # 3. O valor do recurso financiado no SICOR_OPERACAO_BASICA é o 'VL_PARC_CREDITO'
    col_recurso = 'VL_PARC_CREDITO'
    
    # Criar DataFrame padronizado para este ano
    df_padronizado = pd.DataFrame()
    df_padronizado['id_referencia_bacen'] = df_ano[col_bacen].astype(str)
    df_padronizado['nu_ordem'] = df_ano[col_ordem].astype(str)
    
    # Tratamento de valores decimais (substitui vírgula por ponto se necessário)
    if df_ano[col_recurso].dtype == object:
        df_padronizado['vlr_recurso'] = pd.to_numeric(
            df_ano[col_recurso].astype(str).str.replace(',', '.'), errors='coerce'
        )
    else:
        df_padronizado['vlr_recurso'] = pd.to_numeric(df_ano[col_recurso], errors='coerce')
    
    # Criar a coluna 'chavenova' para o Merge
    df_padronizado['chavenova'] = df_padronizado['id_referencia_bacen'] + "_" + df_padronizado['nu_ordem']
    
    # Mapear Programa e Subprograma para filtros de PRONAF (se desejar usar no futuro)
    if 'CD_PROGRAMA' in df_ano.columns:
        df_padronizado['CD_PROGRAMA'] = df_ano['CD_PROGRAMA'].astype(str)
    if 'CD_SUBPROGRAMA' in df_ano.columns:
        df_padronizado['CD_SUBPROGRAMA'] = df_ano['CD_SUBPROGRAMA'].astype(str)

    dfs_operacoes.append(df_padronizado)

# Concatenar todos os anos em um único DataFrame
df_todas_operacoes = pd.concat(dfs_operacoes, ignore_index=True)
print(f"Total de operações locais acumuladas (2016-2026): {df_todas_operacoes.shape[0]} registros.\n")

# ==============================================================================
# 3. LEITURA DO GEOJSON DE GLEBAS E JUNÇÃO (MERGE)
# ==============================================================================
print("2/5. Carregando o GeoJSON de glebas...")
if not os.path.exists(CAMINHO_GEOJSON_GLEBAS):
    raise FileNotFoundError(f"O arquivo GeoJSON de glebas não foi localizado em: {CAMINHO_GEOJSON_GLEBAS}")

gdf_glebas = gpd.read_file(CAMINHO_GEOJSON_GLEBAS)

# Garantir que a chave de ligação esteja como string e sem espaços vazios
gdf_glebas['chavenova'] = gdf_glebas['chavenova'].astype(str).str.strip()
print(f"GeoJSON de glebas carregado com {gdf_glebas.shape[0]} geometrias.")

print("3/5. Realizando o Join (Merge) na memória...")
# Cruzamento das tabelas utilizando a 'chavenova'
gdf_unificado = gdf_glebas.merge(df_todas_operacoes, on='chavenova', how='inner')
print(f"Junção concluída! {gdf_unificado.shape[0]} glebas vinculadas com dados financeiros.\n")

# ==============================================================================
# 4. AGRUPAMENTO MUNICIPAL E NORMALIZAÇÃO (ISVT)
# ==============================================================================
print("4/5. Agrupando e sumarizando os valores financeiros por Município...")

# Nota: Como o SICOR_OPERACAO_BASICA não possui o código do município,
# nós extraímos o código do município diretamente do seu GeoJSON de Glebas!
# Adicionamos 'id_municipio' como a primeira opção de busca com base no feedback do usuário.
colunas_geojson = list(gdf_glebas.columns)
col_municipio_geojson = None

# Busca automática pelo nome da coluna de município no GeoJSON (prioridade para id_municipio)
for nome in ['id_municipio', 'cod_municipio', 'co_municipio', 'cd_mun', 'cd_municipio', 'municipio']:
    for col in colunas_geojson:
        if col.lower() == nome:
            col_municipio_geojson = col
            break
    if col_municipio_geojson:
        break

if not col_municipio_geojson:
    print("[Aviso] Não foi possível identificar automaticamente a coluna de município no GeoJSON.")
    print(f"Colunas disponíveis no GeoJSON: {colunas_geojson}")
    # Define um padrão, ajuste se necessário
    col_municipio_geojson = 'id_municipio' 

print(f"Usando a coluna '{col_municipio_geojson}' do GeoJSON para agrupamento municipal.")

# Agrupando por código do município extraído do GeoJSON
resumo_municipal = gdf_unificado.groupby(col_municipio_geojson).agg(
    volume_total_credito=('vlr_recurso', 'sum'),
    quantidade_contratos=('chavenova', 'count')
).reset_index()

# Renomear a coluna de agrupamento para um padrão limpo
resumo_municipal.rename(columns={col_municipio_geojson: 'cod_municipio'}, inplace=True)
resumo_municipal['cod_municipio'] = resumo_municipal['cod_municipio'].astype(str)

# Aplicar normalização Min-Max (0 a 1) para o indicador do ISVT
v_max = resumo_municipal['volume_total_credito'].max()
v_min = resumo_municipal['volume_total_credito'].min()

if v_max != v_min:
    resumo_municipal['indicador_fomento_normalizado'] = (
        (resumo_municipal['volume_total_credito'] - v_min) / (v_max - v_min)
    )
else:
    resumo_municipal['indicador_fomento_normalizado'] = 1.0

# ==============================================================================
# 5. SALVAMENTO DA SAÍDA
# ==============================================================================
print("5/5. Exportando tabela consolidada...")
resumo_municipal.to_csv(CAMINHO_SAIDA_CSV, index=False, encoding='utf-8-sig')

print(f"\n--- PROCESSO CONCLUÍDO COM SUCESSO! ---")
print(f"Sua tabela leve para o QGIS foi gerada em: {CAMINHO_SAIDA_CSV}")
print("Ela contém os municípios e seu respectivo indicador de fomento normalizado (0 a 1).")
