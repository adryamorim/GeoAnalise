# GeoAnalise


Inteligência Territorial Aplicada ao Desenvolvimento Regional
Identificação de clusters de ecoturismo, economia comunitária e diversificação produtiva para direcionamento estratégico de recursos de desenvolvimento
Este repositório documenta o desenvolvimento de um modelo de Inteligência Territorial voltado para a identificação de "vazios de fomento" e fomento estratégico de recursos públicos no Brasil, com foco em ecoturismo e produção comunitária. O projeto compara duas realidades macroeconômicas brasileiras distintas: os estados da Bahia (BA) e do Rio Grande do Sul (RS).

A tese central deste trabalho propõe que a modelagem espacial é um mecanismo agnóstico capaz de mitigar a assimetria de informação que historicamente gera falhas de mercado e ineficiência na distribuição do crédito rural e de desenvolvimento. Para operacionalizar esta análise, é proposto o Índice Sintético de Viabilidade Territorial (ISVT).

🗺️ Estrutura do Índice Sintético (ISVT)
O ISVT é calculado a partir de um modelo de Análise Multicritério (AHP - Analytic Hierarchy Process) integrado a Sistemas de Informação Geográfica (SIG), baseado em quatro dimensões principais de dados:

Crédito e Fomento Financeiro: Mapeamento da capilaridade e volume de recursos formais (BCB/Sicor/Pronaf/FNE/BRDE).
Demanda e Dinâmica Digital: Utilização de proxies de Big Data para capturar fluxos informais de ecoturismo (Airbnb/Waze).
Estrutura Produtiva Local: Identificação da densidade de prestadores e agentes sociais (Cadastur/MDA/Juntas Comerciais).
Vulnerabilidade e Conectividade: Cruzamento de dados de infraestrutura e vulnerabilidade social (IBGE Censo 2022/Anatel).
🛠️ O que já foi feito (Diário de Bordo & Aprendizados)
Até o momento, o trabalho concentrou-se na estruturação da Dimensão 1: Crédito e Fomento Rural, utilizando os dados espaciais brutos de glebas financiadas pelo Banco Central do Brasil (Sicor) cobrindo a série temporal histórica de 2016 a 2026.

Abaixo está o roteiro passo a passo do fluxo metodológico executado no QGIS:

1. Recorte e Filtros Regionais
Ação: Coleta das malhas municipais do IBGE para RS e BA e filtragem das bases de operações do Sicor para manter apenas os dados correspondentes aos dois estados de interesse (códigos de UF 43 e 29).
2. Consolidação Temporal (Mesclagem)
Ação: Utilização da ferramenta Mesclar Camadas Vetoriais (Merge Vector Layers) no QGIS para unificar os 11 anos de arquivos espaciais brutos de glebas (2016 a 2026) em um único mapa unificado de geometrias históricas.
Aprendizado Técnico: A mesclagem gera uma camada temporária de memória (indicada pelo ícone de chip no QGIS). Essa camada não é editável diretamente e o provedor impede a criação física de novas colunas.
Solução: Exportar a camada mesclada temporária como um arquivo físico permanente no formato GeoPackage (.gpkg) com o SRC definido como SIRGAS 2000 (EPSG:4674).
3. Saneamento Topológico
Ação: Execução do algoritmo Corrigir Geometrias (Fix Geometries) nas glebas históricas mescladas.
Motivo: Glebas cadastradas no Sicor frequentemente possuem imperfeições topológicas (auto-intersecções, vértices duplicados), as quais corrompem e travam análises espaciais avançadas de proximidade e sobreposição.
4. Criação da Chave Composta de Ligação (Join)
Desafio Técnico 1 (Limite de Caracteres): Inicialmente, tentou-se criar a coluna chave_composta. O formato de arquivo antigo (Shapefile) trunca automaticamente qualquer campo com mais de 10 caracteres, gerando erros de gravação.
Solução: Adotar o formato moderno GeoPackage e reduzir o nome do atributo de ligação simplesmente para chave.
Desafio Técnico 2 (Chave Composta e Valores Nulos): O identificador id_referencia_bacen não é único no Sicor, pois uma mesma operação de crédito pode ter múltiplas glebas (diferenciadas pelo número da ordem da gleba, como 1, 2...). Fazer um Join comum apenas por um campo corrompe a correspondência.
Além disso, tentativas iniciais de concatenação simples resultaram em valores inteiramente NULL devido à incompatibilidade de tipos de dados (tentativa de concatenar números como string diretamente).
Solução: Configurar a coluna chave como o tipo Texto (string) na Calculadora de Campo e utilizar uma expressão blindada contra erros de tipo:
concat(to_string("id_referencia_bacen"), '_', to_string("nu_ordem"))
Nota: Se a coluna de ordem da camada de glebas for nomeada de forma diferente (ex: numero_ordem ou nu_seq_gleba), o parâmetro foi devidamente ajustado.

📈 Próximos Passos do Cronograma
[ ] Join das Operações: Executar o mesmo procedimento de criação de chave composta (chave = tipo texto) na planilha tabular de Operações Básicas e realizar a união (Join) com a camada espacial de Glebas no QGIS.
[ ] Consolidação Municipal: Rodar o algoritmo de agregação espacial Unir Atributos por Localização (Resumo) para somar os volumes financeiros aplicados (R$) por município do IBGE.
[ ] Estatística Espacial: Identificar os padrões e clusters espaciais de concessão de crédito rural.
[ ] Cruzamento das Dimensões: Integrar dados de Cadastur e Big Data (Airbnb/Waze) para calibrar o ISVT pelo modelo AHP.
🗄️ Fontes de Dados Mapeadas

Todas as fontes oficiais de dados que alimentarão as próximas fases do TCC estão documentadas no arquivo Relatório de Pesquisa: Fontes de Dados para TCC neste repositório.



Mineração - Aprendizados

Os primeiros dados de crédito rural foram buscados diretamente do site Base dos Dados pois existia um datalake com os dados já tratados. https://basedosdados.org/dataset/544c9d22-97b7-479a-8eca-94762840b465?table=ce7babc2-35b6-4e48-a604-3c4d32306bb3
No Google Cloud, extrai estes dados diretamente através de Big Query (BigQueryBCBRSBA) já trazendo apenas os dados de operações de crédito da Bahia e do Rio Grande do Sul de 2016 a 2026, pois o volume completo dos dados seria muito grande. 

Os dados foram gerados e exportados em json, para trasnformá-los em gejson para que o Qgis pudesse ler, criei o script (convertergeojson)
Ao exportar os dados do big query e transformar em geojson para inserir no qgis, algumas geometrias estavam gerando inconsistências, com cruzamento de pontos que extravasavam os estados analisados.
<img width="362" height="410" alt="image" src="https://github.com/user-attachments/assets/8eabef9b-6788-4851-9339-826d8eb121af" />

Gerei novo código que detecta anomalias nas coordenadas (convertergeojsonv2)
 <img width="886" height="149" alt="image" src="https://github.com/user-attachments/assets/b447c49d-91f0-4ab3-a656-ff786ae55b31" />
Um arquivo informando quais geometrias foram removidas por estado
<img width="886" height="569" alt="image" src="https://github.com/user-attachments/assets/c671f2a1-d773-47e5-a131-471f5d20286c" />



Para esta análise precisamos baixar também as planilhas de Operações Contratadas (SICOR_OPERACAO_BASICA_ESTADO_YYYY.csv) dos mesmos anos. A chave primária composta para unir os dados financeiros (atributos) com os dados espaciais (geometrias) é a junção dos campos id_referencia_bacen + nu_ordem
Como os arquivos são muito extensos, criei o script em Python que filtra todos os csv para que fique apenas com BA e RS (filtrarestados).

<img width="579" height="179" alt="image" src="https://github.com/user-attachments/assets/4f25a6ce-e3d8-4487-a720-017959614f67" />
