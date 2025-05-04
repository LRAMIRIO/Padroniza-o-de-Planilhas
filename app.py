import streamlit as st
import pandas as pd
from io import StringIO
from pathlib import Path

st.set_page_config(page_title="Padronizador de Planilhas", layout="centered")

st.title("📄 Padronizador de Planilhas do INMET")
st.write("Este aplicativo converte arquivos .csv e .xlsx para um formato padronizado (.csv UTF-8 com ponto como separador decimal).")

uploaded_files = st.file_uploader("Envie os arquivos (.csv ou .xlsx)", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            file_suffix = Path(uploaded_file.name).suffix.lower()

            if file_suffix in [".csv"]:
                df = pd.read_csv(uploaded_file, sep=";", encoding="latin1", skip_blank_lines=True, engine="python")
            elif file_suffix in [".xlsx", ".xls"]:
                df = pd.read_excel(uploaded_file)
            else:
                st.warning(f"❌ Formato não suportado: {uploaded_file.name}")
                continue

            # Substitui vírgulas por pontos nas colunas numéricas
            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].astype(str).str.replace(",", ".", regex=False)

            # Tentativa de converter todas as colunas possíveis para numérico
            df = df.apply(pd.to_numeric, errors='ignore')

            # Gerar nome para o arquivo de saída
            output_name = f"{Path(uploaded_file.name).stem}_corrigido.csv"

            # Converter DataFrame para CSV em memória
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, sep=";", index=False, encoding="utf-8")
            st.download_button(label=f"📥 Baixar {output_name}", data=csv_buffer.getvalue(), file_name=output_name, mime="text/csv")
        except Exception as e:
            st.error(f"Erro ao processar {uploaded_file.name}: {e}")