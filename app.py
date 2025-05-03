
import streamlit as st

st.set_page_config(page_title="Corretor de CSV INMET", layout="centered")

st.title("🛠️ Correção de Arquivos CSV do INMET")
st.write("Este aplicativo remove os ';' extras no cabeçalho dos arquivos CSV do INMET, facilitando sua leitura no Excel e em scripts automatizados.")

uploaded_files = st.file_uploader(
    "📤 Envie um ou mais arquivos CSV para corrigir",
    type="csv",
    accept_multiple_files=True,
    key="csv_corrigir"
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        lines = uploaded_file.getvalue().decode("latin1").splitlines()
        corrected_lines = [line.rstrip(';') for line in lines[:8]] + lines[8:]
        corrected_content = "\n".join(corrected_lines)
        corrected_filename = "corrigido_" + uploaded_file.name

        st.download_button(
            label=f"📥 Baixar arquivo corrigido: {corrected_filename}",
            data=corrected_content.encode("latin1"),
            file_name=corrected_filename,
            mime="text/csv"
        )
