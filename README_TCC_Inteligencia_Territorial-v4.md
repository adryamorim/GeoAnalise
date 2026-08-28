# Inteligência Territorial Aplicada ao Desenvolvimento Regional
## Identificação de clusters de ecoturismo, economia comunitária e diversificação produtiva para direcionamento estratégico de recursos de desenvolvimento

Este repositório documenta o desenvolvimento de um modelo de **Inteligência Territorial** voltado para a identificação de "vazios de fomento" e direcionamento estratégico de recursos de desenvolvimento regional no Brasil. O projeto compara duas realidades macroeconômicas brasileiras distintas: os estados da **Bahia (BA)** e do **Rio Grande do Sul (RS)**.

A tese central deste trabalho propõe que a modelagem espacial é um mecanismo agnóstico capaz de mitigar a assimetria de informação que historicamente gera falhas de mercado e ineficiência na distribuição do crédito rural e de desenvolvimento. Para operacionalizar esta análise, é proposto o **Índice Sintético de Viabilidade Territorial (ISVT)**.

---

## 🗺️ Estrutura do Índice Sintético (ISVT)

O ISVT é calculado a partir de um modelo de **Análise Multicritério** integrado a Sistemas de Informação Geográfica (SIG), baseado em quatro dimensões principais de dados:

1. **Fomento Financeiro e Densidade de Capital:** Mapeamento da capilaridade e volume de recursos formais e de longo prazo (BCB/SICOR/BNDES).
2. **Demanda e Dinâmica Digital:** Utilização de proxies de Big Data para capturar fluxos informais de turismo (Airbnb/Waze).
3. **Estrutura Produtiva Local:** Identificação da densidade de prestadores e agentes sociais (Cadastur/MDA/Juntas Comerciais).
4. **Vulnerabilidade e Conectividade:** Cruzamento de dados de infraestrutura e vulnerabilidade social (IBGE Censo 2022/Anatel).

---

## 🎯 Por que cruzar os dados do BNDES e do SICOR? (Marco Teórico e Metodológico)

No desenvolvimento do **ISVT Dimensão 1**, o cruzamento entre as bases de dados do **SICOR (Banco Central)** e do **BNDES** é um dos pilares mais inovadores e teoricamente fundamentados deste TCC. Essa integração responde a questões profundas de economia regional e desenvolvimento territorial:

### 1. A Dicotomia "Finance" vs. "Funding" (Pós-Keynesianismo)
Apoiando-se na teoria pós-keynesiana de desenvolvimento (Studart, 1993/1995; Paula et al., 2023), identificamos que o fomento regional de um território depende de duas forças complementares:
*   **SICOR (Crédito Rural/Agricultural):** Representa a provisão de liquidez de curto prazo (*Finance*). Trata-se de recursos direcionados para custeio agropecuário, custeio de safra e investimento de varejo (como o PRONAF). É extremamente capilarizado e irriga diretamente as famílias produtoras na ponta, as quais constituem a espinha dorsal do **turismo rural e comunitário**.
*   **BNDES (Fomento Regional/Estruturante):** Representa o investimento e captação de longo prazo (*Funding*). São recursos aplicados em infraestrutura, saneamento, grandes redes logísticas, hotelaria, comércio e serviços não agrícolas.

### 2. Evitando o Viés do "Vazio Produtivo"
Se analisássemos apenas o **SICOR**, concluiríamos erroneamente que os municípios industriais ou puramente turísticos urbanos são vazios econômicos (pois possuem pouca atividade agropecuária). Se analisássemos apenas o **BNDES**, ignoraríamos a força da agricultura familiar e do ecoturismo rural, pois os microcréditos descentralizados são repassados por cooperativas (e muitas vezes não constam como grandes obras diretas). O cruzamento unificado anula esse viés, fornecendo uma visão fidedigna da **Densidade de Capital** do território.

### 3. Eliminação do Viés de Transferência Regional
Para comparar Bahia (BA) e Rio Grande do Sul (RS) de forma científica, **não podemos usar fundos regionais exclusivos**, como o **FNE** (Fundo Constitucional do Nordeste), que atua apenas na Bahia. Como o BNDES e o Banco Central (SICOR) possuem atuação de abrangência nacional, a sua integração garante uma régua de medição justa e equitativa entre as regiões Norte/Nordeste e Sul do país.

---

## 🛠️ Evolução Metodológica e Tecnológica (Rigor Metodológico V4)

Após discussões técnicas e testes práticos no ambiente do Google Colab, o pipeline foi refinado de uma estrutura em nuvem para uma **solução 100% offline e auto-higienizável**:

### 1. Migração da Nuvem (BigQuery) para o Processamento Local
Anteriormente, o script conectava-se à API da *Base dos Dados* via Google BigQuery. Contudo, devido a barreiras de autenticação de terceiros, controle de permissões IAM e exigência de vinculação de faturamento (GCP Billing Account) que geravam o erro `403 Forbidden`, a arquitetura foi convertida para **local offline**. 

### 2. Otimização de Memória via Leitura em Blocos (Chunking)
A planilha unificada oficial do BNDES (`desembolsos-mensais.csv`) contém todo o histórico brasileiro de 1995 a 2026, totalizando cerca de **719.6 MB**. Para rodar no Google Colab sem esgotar a memória RAM e sofrer travamento de sessão, o código lê o arquivo em fluxos de **100.000 linhas por vez** (*chunks*), filtrando em tempo real e descartando dados irrelevantes na hora.

### 3. Blindagem de Parser e Higienização de Aspas (`QUOTE_NONE` + `Auto-Clean`)
Em bases brutas governamentais, aspas soltas (ex: nomes de empresas ou cidades com aspas simples/duplas não fechadas) quebram o interpretador do Pandas, causando o erro `ParserError: EOF inside string`. 
*   **Solução técnica:** O script usa `quoting=csv.QUOTE_NONE` para desativar a leitura especial de aspas.
*   **Auto-Clean de Aspas Físicas:** Como efeito colateral, strings e números vêm envelopados em aspas literais (ex: a célula lê `'"BA"'` em vez de `'BA'`). O script **higieniza fisicamente** todos os dados no nível de bloco (colunas e valores textuais), garantindo que as seleções temporais e espaciais funcionem sem gerar dados vazios ou zerados.

### 4. Auto-Detecção de Delimitador Físico
O script analisa os primeiros bytes do arquivo para identificar automaticamente se a planilha está separada por ponto e vírgula (`;`), vírgula (`,`) ou tabulações (`	`), ajustando também o separador decimal proporcionalmente.

### 5. Análise Temporal Dinâmica
Basta alterar a variável global `ANO_ANALISE = 2024` ou `2025` no topo do notebook para que todo o fomento financeiro, rankings e mapas sejam recalculados instantaneamente para aquele momento histórico específico.

### 6. Exportação de Mapas em Alta Resolução e Vetor
O pipeline salva de forma autônoma os mapas do ISVT em dois formatos:
*   **PNG (300 DPI):** Resolução profissional ideal para o corpo de texto do Word.
*   **PDF Vetorial:** Zoom infinito ideal para impressão física e análise de detalhes da malha municipal.

---

## 📂 Organização dos Arquivos de Código

O repositório está dividido nas seguintes etapas integradas:

### Engenharia de Dados (Local / VS Code)
* `processamento_local_sicor_v6.py`: Script para limpeza e georreferenciamento de dados brutos agrícolas. Gera o arquivo consolidado `Fomento_Municipal_Anual_WIDE.csv`.

### Modelagem e Análise (Google Colab)
* `analise_isvt_dimensao1_revisada_v16.py`: Versão definitiva da Dimensão 1. Processamento em blocos offline, limpeza física de aspas nas strings, cálculo de consistência AHP de Saaty, log-transform, normalização intra-estado e geração de mapas/PDFs vetoriais por ano.
* `analise_isvt_dimensao2_colab.py`: Processamento da Dimensão 2 (Airbnb). Realiza o cruzamento espacial geométrico de pontos e polígonos municipais (Spatial Join).

---

## 📖 Fundamentação Teórica para Escrita do TCC

| Conceito / Indicador | Teoria de Suporte | Autores de Referência | Aplicação no TCC |
| :--- | :--- | :--- | :--- |
| **Finance vs. Funding** | Teoria Monetária da Produção | Keynes (1937), Studart (1995), Paula et al. (2023) | Justifica a separação analítica e pesos diferenciados entre crédito de varejo (SICOR) e recursos de longo prazo (BNDES/FNE). |
| **Heterogeneidade Estrutural** | Teoria do Subdesenvolvimento da CEPAL | Aníbal Pinto, Celso Furtado, Bielschowsky | Fundamenta estatisticamente a necessidade do log-transform ($np.log1p$) e da normalização intra-estado para captar as disparidades do interior. |
| **Intervenção do Estado** | Papel dos Bancos de Desenvolvimento | Araújo (2018), Fochezatto (2026), BNDES | Sustenta o uso do indicador de "Fomento Regional" como canal de redução de falhas de mercado territoriais. |
| **Análise Espacial (SIG)** | Primeira Lei da Geografia / Autocorrelação | Tobler (1970), Anselin (LISA), PySAL | Embasamento metodológico para o uso do Geopandas, agrupamento por polígonos e futura análise de clusters espaciais. |

---
*Documentação de Progresso revisada e atualizada com rigor acadêmico em agosto de 2026.*
