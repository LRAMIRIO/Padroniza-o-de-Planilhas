
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Validador de Planilhas", layout="wide")

st.title("✅ Validador de Planilhas INMET")

arquivos = st.file_uploader("Envie os arquivos (.csv, .xls, .xlsx)", accept_multiple_files=True)

if arquivos:
    for arquivo in arquivos:
        nome = arquivo.name
        st.subheader(f"📄 {nome}")
        try:
            nome_lower = nome.lower()
            if nome_lower.endswith((".csv", ".txt")):
                df = pd.read_csv(arquivo, sep=";", encoding="latin1", skiprows=8)
            elif nome_lower.endswith((".xlsx", ".xls")):
                df = pd.read_excel(arquivo)
            else:
                st.warning(f"Tipo de arquivo não suportado: {nome}")
                continue

            st.success(f"Arquivo {nome} carregado com sucesso!")
            st.dataframe(df.head())

        except Exception as e:
            st.error(f"Erro ao processar {nome}: {e}")
