# Conversor de Extensão para CSV (Streamlit)

Este aplicativo permite converter arquivos `.csv`, `.xls` e `.xlsx` para o formato `.csv`, mantendo a estrutura e os dados originais intactos.

## Funcionalidades
- Aceita até 15 arquivos por vez;
- Converte `.xls` e `.xlsx` para `.csv` com separador `;`;
- Mantém `.csv` como estão, apenas uniformizando a extensão;
- Gera um arquivo `.zip` com os resultados.

## Como usar
1. Suba seus arquivos no campo de upload;
2. Aguarde a conversão;
3. Baixe o `.zip` com os arquivos `.csv` corrigidos.

## Execução local
```bash
pip install -r requirements.txt
streamlit run app.py
```