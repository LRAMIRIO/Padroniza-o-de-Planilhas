
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Conversor de Planilhas para CSV", layout="centered")

st.title("📄 Conversor de Planilhas Excel para CSV")

st.write("Este aplicativo permite enviar arquivos `.xls`, `.xlsx` ou `.csv` (separado por ponto e vírgula) e converte todos para `.csv` corrigido com codificação UTF-8 e separador vírgula.")

uploaded_files = st.file_uploader("Envie suas planilhas", accept_multiple_files=True, type=['xls', 'xlsx', 'csv'])

if uploaded_files:
    for file in uploaded_files:
        st.subheader(f"📥 Arquivo enviado: `{file.name}`")
        try:
            if file.name.lower().endswith('.csv'):
                df = pd.read_csv(file, sep=';', encoding='latin1')
            else:
                df = pd.read_excel(file)

            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False, encoding='utf-8', sep=',')

            st.download_button(
                label=f"⬇️ Baixar `{file.name.rsplit('.', 1)[0]}.csv`",
                data=csv_buffer.getvalue(),
                file_name=f"{file.name.rsplit('.', 1)[0]}.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"Erro ao processar `{file.name}`: {str(e)}")
