# GeoAnalise

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
