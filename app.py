import streamlit as st
import pandas as pd
from io import StringIO
from pathlib import Path
import base64
import os

st.set_page_config(page_title="Corretor de Arquivos CSV do INMET", layout="centered")
st.title("🛠️ Corretor de Arquivos CSV do INMET")
st.write("Este aplicativo corrige arquivos CSV do INMET com cabeçalhos inconsistentes e converte em arquivos limpos para análise.")

# Upload dos arquivos
uploaded_files = st.file_uploader("📁 Envie os arquivos CSV ou Excel", accept_multiple_files=True, type=["csv", "CSV", "xls", "xlsx"])

# Função para detectar separador
def detectar_sep(linha):
    if ';' in linha:
        return ';'
    elif ',' in linha:
        return ','
    else:
        return ';'  # padrão

# Processamento
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.markdown(f"---\n### 📄 Arquivo: `{uploaded_file.name}`")
        try:
            content = uploaded_file.read().decode('latin1')
            linhas = content.splitlines()

            # Detectar separador na linha 9
            sep = detectar_sep(linhas[8])
            colunas = linhas[8].strip().split(sep)
            dados = linhas[9:]

            # Recriar conteúdo limpo
            csv_limpo = StringIO()
            csv_limpo.write(sep.join(colunas) + '\n')
            csv_limpo.write('\n'.join(dados))
            csv_limpo.seek(0)

            # Ler com pandas e exibir preview
            df = pd.read_csv(csv_limpo, sep=sep)
            st.success("Arquivo corrigido com sucesso!")
            st.dataframe(df.head())

            # Preparar para download
            nome_saida = Path(uploaded_file.name).stem + "_corrigido.csv"
            csv_corrigido = df.to_csv(index=False, sep=';').encode('utf-8')
            b64 = base64.b64encode(csv_corrigido).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="{nome_saida}">📥 Baixar arquivo corrigido</a>'
            st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Erro ao processar {uploaded_file.name}: {e}")
