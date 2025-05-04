
# Conversor IBUTG

Este app em Streamlit converte planilhas de dados meteorológicos do INMET para o formato compatível com o modelo IBUTG.

## Funcionalidades

- Detecta automaticamente o fuso horário da cidade a partir da latitude/longitude no cabeçalho do CSV.
- Filtra os dados entre 08:00 e 17:00 no horário local.
- Preenche os dados na planilha de modelo IBUTG (colunas DATA, HORA, TAR, TPO, UR, VENTO).
- Permite baixar os resultados em formato `.xlsx`.

## Como usar

1. Faça upload da planilha modelo `Modelo.xlsx`.
2. Faça upload dos arquivos CSV do INMET.
3. O sistema processa, converte e permite o download das planilhas formatadas.

## Requisitos

- Python 3.8+
- Bibliotecas: streamlit, pandas, openpyxl, pytz, timezonefinder
