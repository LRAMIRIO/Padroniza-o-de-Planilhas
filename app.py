import streamlit as st
import pandas as pd
from pathlib import Path
import io

st.set_page_config(page_title="Padronizador de Planilhas INMET", layout="centered")

st.title("📄 Padronizador de Planilhas INMET")
st.write("Esse aplicativo permite carregar arquivos do INMET (.csv, .xls, .xlsx), padronizar colunas e corrigir problemas de codificação.")

uploaded_file = st.file_uploader("🔼 Envie seu arquivo", type=None)

if uploaded_file is not None:
    file_suffix = Path(uploaded_file.name).suffix.lower()

    try:
        if file_suffix == ".csv":
            df = pd.read_csv(uploaded_file, sep=';', encoding='latin1', skiprows=8, low_memory=False)
        elif file_suffix in [".xls", ".xlsx"]:
            df = pd.read_excel(uploaded_file)
        else:
            st.warning("⚠️ Tipo de arquivo não reconhecido. Tentando abrir como CSV com encoding padrão...")
            df = pd.read_csv(uploaded_file, sep=';', encoding='latin1', skiprows=8, low_memory=False)
    except Exception as e:
        st.error(f"❌ Erro ao ler o arquivo: {e}")
        st.stop()

    st.success("✅ Arquivo carregado com sucesso!")
    st.dataframe(df.head())

    # Botão para download em CSV padronizado
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, sep=';', encoding='utf-8')
    st.download_button(
        label="⬇️ Baixar arquivo corrigido (.csv)",
        data=csv_buffer.getvalue(),
        file_name=f"corrigido_{uploaded_file.name.replace(' ', '_')}.csv",
        mime="text/csv"
    )
