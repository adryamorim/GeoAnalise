# Relatório de Pesquisa: Fontes de Dados para TCC de Inteligência Territorial

Esta pesquisa identifica onde e como obter as bases de dados e microdados necessários para o desenvolvimento do Trabalho de Conclusão de Curso (TCC) intitulado **"Inteligência territorial aplicada ao desenvolvimento regional: identificação de clusters de ecoturismo, economia comunitária e diversificação produtiva para direcionamento estratégico de recursos de desenvolvimento"**, com foco comparativo entre os estados do Rio Grande do Sul (RS) e da Bahia (BA).

As fontes estão mapeadas e organizadas por eixos temáticos em conformidade com o Índice Sintético de Viabilidade Territorial (ISVT).

---

## 🏛️ Crédito Rural e Fomento Financeiro

| # | Título | Órgão/Plataforma | Link de Acesso |
|---|--------|------------------|----------------|
| 1 | Tabelas e Microdados do Crédito Rural e do Proagro | Banco Central do Brasil (BCB) | [Acessar](https://www.bcb.gov.br/estabilidadefinanceira/tabelas-credito-rural-proagro) |
| 2 | Matriz de Dados do Crédito Rural (MDCR) | Dados Abertos BCB | [Acessar](https://dadosabertos.bcb.gov.br/dataset/matrizdadoscreditorural) |
| 3 | Guia Técnico de Modelagem de Microdados do Sicor | GeoCreditoRural (GitHub) | [Acessar](https://geo-credito-rural.github.io/sicor/microdados/index.html) |
| 4 | Microdados do Sicor Tratados e Unificados | Base dos Dados | [Acessar](https://basedosdados.org/dataset/544c9d22-97b7-479a-8eca-94762840b465) |

### Descrição Detalhada das Fontes de Crédito:
*   **Tabelas e Microdados do Crédito Rural e do Proagro:** Fornece microdados brutos do Sistema de Operações do Crédito Rural e do Proagro (Sicor) desde 2013 em formato CSV, o que permite cruzar operações financeiras com as coordenadas geográficas de glebas e propriedades no QGIS.
*   **Matriz de Dados do Crédito Rural (MDCR):** Disponibiliza dados agregados sobre concessão de crédito de forma mensal e diária. É excelente para obter volumes consolidados por município, programa de financiamento (como o Pronaf) e tipo de pessoa. Possui uma API estruturada e navegação amigável.
*   **GeoCreditoRural (GitHub):** Uma documentação inestimável criada por pesquisadores que ensina passo a passo a processar, validar e limpar as geometrias e tabelas do Sicor/BCB dentro do ambiente QGIS/PostGIS, poupando meses de trabalho metodológico.
*   **Base dos Dados - Microdados do Sicor:** Facilita a consulta em nuvem de dados estruturados e limpos do Sicor usando linguagens como SQL (via BigQuery), Python ou R, reduzindo drasticamente o esforço computacional local.

---

## 🗺️ Ecoturismo, Empreendimentos e Serviços Turísticos

| # | Título | Órgão/Plataforma | Link de Acesso |
|---|--------|------------------|----------------|
| 1 | Portal de Dados Abertos do Turismo (Cadastur) | Ministério do Turismo (MTur) | [Acessar](https://dados.turismo.gov.br/dataset/) |
| 2 | Hotsite e Consulta de Prestadores Cadastur | Cadastur | [Acessar](https://cadastur.turismo.gov.br/hotsite/) |

### Descrição Detalhada das Fontes de Turismo:
*   **Portal de Dados Abertos do Turismo (Cadastur):** Fornece arquivos em formatos abertos (CSV, XLS, XLSX) com dados completos e catalogados de prestadores de serviços de turismo em atividade no país. Os conjuntos estão divididos por categorias-chave como Meios de Hospedagem, Guias de Turismo, Parques Temáticos e Acampamentos Turísticos.
*   **Hotsite e Consulta de Prestadores Cadastur:** Permite realizar consultas individuais de prestadores regulares, servindo para entender o dicionário de variáveis e os critérios de validação das operações locais.

---

## 📈 Dados Demográficos, Socioeconômicos e Vetores Espaciais

| # | Título | Órgão/Plataforma | Link de Acesso |
|---|--------|------------------|----------------|
| 1 | Painel de Resultados do Censo Demográfico 2022 | IBGE | [Acessar](https://www.ibge.gov.br/estatisticas/sociais/trabalho/22827-censo-demografico-2022.html) |
| 2 | Cadastro Nacional de Endereços para Fins Estatísticos (CNEFE) | IBGE | [Acessar](https://www.ibge.gov.br/estatisticas/sociais/populacao/38734-cadastro-nacional-de-enderecos-para-fins-estatisticos.html) |
| 3 | Malhas Territoriais e Setores Censitários (Censo 2022) | IBGE / Geociências | [Acessar](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/26565-malhas-de-setores-censitarios-divisoes-intramunicipais.html) |
| 4 | Censo 2022 Integrado e Facilitado | Base dos Dados | [Acessar](https://basedosdados.org/dataset/08a1546e-251f-4546-9fe0-b1e6ab2b203d) |

### Descrição Detalhada das Fontes de Dados Demográficos:
*   **Painel do Censo Demográfico 2022:** É o portal oficial de divulgação de resultados do Censo 2022, provendo o acesso direto ao sistema SIDRA para a extração de dados tabulares de população, renda domiciliar, saneamento e IDH-M.
*   **Cadastro Nacional de Endereços para Fins Estatísticos (CNEFE):** O CNEFE provê microdados georreferenciados de todos os mais de 106 milhões de endereços cadastrados no Censo, o que permite fazer o mapeamento espacial de extrema resolução e identificar com precisão a estrutura das comunidades no QGIS.
*   **Malhas de Setores Censitários:** Fornece os arquivos vetoriais (Shapefiles ou GeoPackage) que delimitam espacialmente cada setor censitário do Brasil por UF (incluindo Bahia e Rio Grande do Sul). É a malha cartográfica essencial para plotar e correlacionar os seus dados no QGIS.
*   **Censo 2022 - Base dos Dados:** Permite consultar tabelas consolidadas do Censo 2022 limpas e organizadas de forma otimizada para integração via SQL ou Python.

---

## 📱 Conectividade e Infraestrutura de Telecomunicações

| # | Título | Órgão/Plataforma | Link de Acesso |
|---|--------|------------------|----------------|
| 1 | Painel de Cobertura Móvel Nacional | Anatel | [Acessar](https://informacoes.anatel.gov.br/paineis/infraestrutura/cobertura-movel) |
| 2 | Mosaico - Consulta de Sinal de Celular e Mapas | Anatel / Mosaico | [Acessar](https://sistemas.anatel.gov.br/se/public/cmap.php) |
| 3 | Mapa de Estações Radiobase (ERBs) do Brasil | Conexis Brasil | [Acessar](https://conexis.org.br/numeros/mapa-de-antenas/) |

### Descrição Detalhada das Fontes de Conectividade:
*   **Painel de Cobertura Móvel Nacional:** Apresenta os percentuais de cobertura das tecnologias 2G, 3G, 4G e 5G em termos de população, domicílios e área geográfica para cada município brasileiro.
*   **Mosaico Anatel:** Fornece predições de nível de sinal teóricos baseados nas coordenadas e dados técnicos das antenas operacionais, permitindo baixar arquivos de cobertura para subsidiar análises de conectividade em áreas rurais de difícil acesso.
*   **Mapa de Antenas (Conexis):** Permite visualizar o quantitativo e a exata geolocalização de cada Estação Rádio Base (ERB) instalada e licenciada no país, o que é fantástico para realizar análises de densidade e proximidade a infraestruturas de comunicação no QGIS.

---

## 🚜 Agricultura Familiar e Produtores Locais

| # | Título | Órgão/Plataforma | Link de Acesso |
|---|--------|------------------|----------------|
| 1 | Portal e Consulta Pública de Unidades Familiares (CAF) | Ministério do Desenvolvimento Agrário (MDA) | [Acessar](https://caf.mda.gov.br/) |
| 2 | Cadastro da Agricultura Familiar (CAF) e DAP-Web | Governo Federal / MDA | [Acessar](https://dap.mda.gov.br/) |
| 3 | Resultados Municipais do Censo Agropecuário 2017 | IBGE / Censo Agro | [Acessar](https://censoagro2017.ibge.gov.br/resultados-censo-agro-2017.html) |

### Descrição Detalhada das Fontes de Agricultura Familiar:
*   **CAF - Cadastro Nacional da Agricultura Familiar:** Portal oficial de emissão e gestão do CAF (que substituiu a DAP desde 2022). Permite a consulta de unidades familiares e de empreendimentos comunitários rurais legítimos aptos a acessar fomento.
*   **Cadastro da Agricultura Familiar e DAP-Web:** Fornece o histórico e as bases de transição de aptidão (DAP para CAF-Pronaf), necessárias para monitorar a evolução dos produtores cadastrados.
*   **Censo Agropecuário 2017:** Provê os dados consolidados no nível municipal sobre estabelecimentos familiares, produção agropecuária regional, gênero de produtores e cooperativismo rural.

---

## 📊 Big Data e Dinâmicas de Demanda Digital

| # | Título | Órgão/Plataforma | Link de Acesso |
|---|--------|------------------|----------------|
| 1 | Portal de Microdados de Hospedagens e Avaliações | Inside Airbnb | [Acessar](https://insideairbnb.com/get-the-data/) |
| 2 | Portal Waze for Cities | Waze Partnership | [Acessar](https://www.waze.com/pt-BR/wazeforcities/) |

### Descrição Detalhada das Fontes de Big Data:
*   **Inside Airbnb (Get the Data):** Uma das fontes globais mais respeitadas de dados abertos extraídos da plataforma Airbnb. Disponibiliza arquivos CSV contendo preços, coordenadas geográficas precisas, avaliações dos clientes e características das locações por temporada no Brasil (abrangendo destinos turísticos consolidados de BA e RS).
*   **Waze for Cities:** Programa de parceria gratuito do Google que compartilha dados de tráfego, congestionamento e incidentes em tempo real e históricos com instituições parceiras e governos. É a fonte perfeita para criar indicadores de acessibilidade viária e atração de fluxos regionais.

---

## Diretrizes Práticas de Integração no QGIS para o TCC

Ao obter esses dados brutos, o fluxo de trabalho de Geoprocessamento recomendado para a elaboração do ISVT é:
1.  **Padronização do Sistema de Referência Geográfico:** Certifique-se de configurar todos os dados vetoriais e matriciais na projeção **SIRGAS 2000 (EPSG:4674)** para evitar distorções de cálculo em BA e RS.
2.  **Junção de Tabelas (Table Join):** Utilize os códigos de municípios e setores censitários do IBGE (que são códigos de 7 e 15 dígitos respectivamente) como chaves primárias unificadas para ligar os dados tabulares da Anatel, do Censo 2022 e do Censo Agropecuário com as respectivas geometrias vetoriais da malha do IBGE.
3.  **Conversão de Pontos para Vetor (Glebas e Antenas):** Utilize as ferramentas "Criar Camada de Pontos a partir de Tabela" no QGIS usando as coordenadas de Latitude e Longitude obtidas dos microdados do Sicor, do Cadastur e do Inside Airbnb.
4.  **Cálculo Multicritério (AHP):** Utilize o plugin **Easy AHP** ou o **AHP Calculator** no QGIS (ou execute o algoritmo em Python usando bibliotecas como pandas e geopandas) para ponderar cada camada conforme os pesos definidos pelos especialistas, gerando o raster ou mapa vetorial final do ISVT.
