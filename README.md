# Padronizador de Planilhas INMET

Este aplicativo Streamlit permite carregar arquivos `.csv` ou `.xlsx` e converte-os para arquivos `.csv` padronizados com codificação UTF-8, separador `;` e vírgula substituída por ponto nas colunas numéricas.

## Funcionalidades:
- Suporte a múltiplos arquivos.
- Conversão automática de colunas numéricas com vírgula para ponto.
- Geração de arquivos corrigidos prontos para uso.
- Compatível com planilhas do INMET e outras planilhas similares.

## Como utilizar:
1. Faça upload de arquivos .csv ou .xlsx.
2. Baixe os arquivos corrigidos individualmente em formato `.csv`.

## Requisitos:
- streamlit
- pandas
- openpyxl

Ideal para pesquisadores, engenheiros ambientais e profissionais que lidam com dados meteorológicos.