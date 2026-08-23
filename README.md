# Inteligência Territorial Aplicada ao Desenvolvimento Regional
## Identificação de clusters de ecoturismo, economia comunitária e diversificação produtiva para direcionamento estratégico de recursos de desenvolvimento

Este repositório documenta o desenvolvimento de um modelo de **Inteligência Territorial** voltado para a identificação de "vazios de fomento" e fomento estratégico de recursos públicos no Brasil, com foco em ecoturismo e produção comunitária. O projeto compara duas realidades macroeconômicas brasileiras distintas: os estados da **Bahia (BA)** e do **Rio Grande do Sul (RS)**.

A tese central deste trabalho propõe que a modelagem espacial é um mecanismo agnóstico capaz de mitigar a assimetria de informação que historicamente gera falhas de mercado e ineficiência na distribuição do crédito rural e de desenvolvimento. Para operacionalizar esta análise, é proposto o **Índice Sintético de Viabilidade Territorial (ISVT)**.

---

## 🗺️ Estrutura do Índice Sintético (ISVT)

O ISVT é calculado a partir de um modelo de **Análise Multicritério (AHP - Analytic Hierarchy Process)** integrado a Sistemas de Informação Geográfica (SIG), baseado em quatro dimensões principais de dados:

1. **Crédito e Fomento Financeiro:** Mapeamento da capilaridade e volume de recursos formais (BCB/Sicor/Pronaf/FNE/BRDE).
2. **Demanda e Dinâmica Digital:** Utilização de proxies de Big Data para capturar fluxos informais de ecoturismo (Airbnb/Waze).
3. **Estrutura Produtiva Local:** Identificação da densidade de prestadores e agentes sociais (Cadastur/MDA/Juntas Comerciais).
4. **Vulnerabilidade e Conectividade:** Cruzamento de dados de infraestrutura e vulnerabilidade social (IBGE Censo 2022/Anatel).

---

## 🛠️ O que já foi feito (Diário de Bordo & Aprendizados)

Até o momento, o trabalho concentrou-se na estruturação da **Dimensão 1: Crédito e Fomento Rural**, utilizando os dados espaciais brutos de glebas financiadas pelo Banco Central do Brasil (Sicor) cobrindo a série temporal histórica de **2016 a 2026**.

Abaixo está o roteiro passo a passo do fluxo metodológico executado no **QGIS**:

### 1. Recorte e Filtros Regionais
* **Ação:** Coleta das malhas municipais do IBGE para RS e BA e filtragem das bases de operações do Sicor para manter apenas os dados correspondentes aos dois estados de interesse (códigos de UF `43` e `29`).

### 2. Consolidação Temporal (Mesclagem)
* **Ação:** Utilização da ferramenta *Mesclar Camadas Vetoriais* (Merge Vector Layers) no QGIS para unificar os 11 anos de arquivos espaciais brutos de glebas (`2016` a `2026`) em um único mapa unificado de geometrias históricas.
* **Aprendizado Técnico:** A mesclagem gera uma camada temporária de memória (indicada pelo ícone de chip no QGIS). Essa camada não é editável diretamente e o provedor impede a criação física de novas colunas.
* **Solução:** Exportar a camada mesclada temporária como um arquivo físico permanente no formato **GeoPackage (`.gpkg`)** com o SRC definido como **SIRGAS 2000 (EPSG:4674)**.

### 3. Saneamento Topológico
* **Ação:** Execução do algoritmo *Corrigir Geometrias* (Fix Geometries) nas glebas históricas mescladas.
* **Motivo:** Glebas cadastradas no Sicor frequentemente possuem imperfeições topológicas (auto-intersecções, vértices duplicados), as quais corrompem e travam análises espaciais avançadas de proximidade e sobreposição.

### 4. Criação da Chave Composta de Ligação (Join)
* **Desafio Técnico 1 (Limite de Caracteres):** Inicialmente, tentou-se criar a coluna `chave_composta`. O formato de arquivo antigo (Shapefile) trunca automaticamente qualquer campo com mais de 10 caracteres, gerando erros de gravação.
  * **Solução:** Adotar o formato moderno GeoPackage e reduzir o nome do atributo de ligação simplesmente para **`chave`**.
* **Desafio Técnico 2 (Chave Composta e Valores Nulos):** O identificador `id_referencia_bacen` não é único no Sicor, pois uma mesma operação de crédito pode ter múltiplas glebas (diferenciadas pelo número da ordem da gleba, como `1`, `2`...). Fazer um Join comum apenas por um campo corrompe a correspondência.
  * Além disso, tentativas iniciais de concatenação simples resultaram em valores inteiramente `NULL` devido à incompatibilidade de tipos de dados (tentativa de concatenar números como string diretamente).
  * **Solução:** Configurar a coluna `chave` como o tipo **Texto (string)** na Calculadora de Campo e utilizar uma expressão blindada contra erros de tipo:
    ```sql
    concat(to_string("id_referencia_bacen"), '_', to_string("nu_ordem"))
    ```
    *Nota: Se a coluna de ordem da camada de glebas for nomeada de forma diferente (ex: `numero_ordem` ou `nu_seq_gleba`), o parâmetro foi devidamente ajustado.*

---

## 📈 Próximos Passos do Cronograma

- [ ] **Join das Operações:** Executar o mesmo procedimento de criação de chave composta (`chave` = tipo texto) na planilha tabular de *Operações Básicas* e realizar a união (*Join*) com a camada espacial de Glebas no QGIS.
- [ ] **Consolidação Municipal:** Rodar o algoritmo de agregação espacial *Unir Atributos por Localização (Resumo)* para somar os volumes financeiros aplicados (R$) por município do IBGE.
- [ ] **Estatística Espacial:** Identificar os padrões e *clusters* espaciais de concessão de crédito rural.
- [ ] **Cruzamento das Dimensões:** Integrar dados de Cadastur e Big Data (Airbnb/Waze) para calibrar o ISVT pelo modelo AHP.

---

## 🗄️ Fontes de Dados Mapeadas

Todas as fontes oficiais de dados que alimentarão as próximas fases do TCC estão documentadas no arquivo `Relatório de Pesquisa: Fontes de Dados para TCC` neste repositório.

---
*Documentação de Progresso atualizada em agosto de 2026.*
