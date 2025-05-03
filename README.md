
# 🛠️ Corretor de Arquivos CSV para Streamlit

Este aplicativo web corrige arquivos `.csv` que possam estar com codificação ou estrutura incorreta para uso em outros aplicativos Streamlit.

## Funcionalidades

- Corrige arquivos `.csv` com codificação `latin1` e reexporta como `UTF-8`.
- Substitui espaços nos nomes dos arquivos por "_".
- Disponibiliza os arquivos corrigidos para download diretamente no app.

## Como utilizar no Streamlit Cloud

1. Crie um repositório no GitHub e envie os arquivos `app.py`, `requirements.txt` e `README.md`.
2. Acesse https://streamlit.io/cloud.
3. Faça login com o GitHub.
4. Clique em "New app", selecione o repositório e o arquivo `app.py`.
5. Clique em "Deploy".

## Requisitos

- `streamlit`
- `pandas`
