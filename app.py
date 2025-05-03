
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Corrigir CSV INMET", layout="centered")

st.title("🔧 Corrigir arquivos CSV do INMET com cabeçalho inválido")
st.markdown("""
Este aplicativo remove ponto e vírgula desnecessário no cabeçalho dos arquivos `.CSV` do INMET que causam erro ao abrir no Excel ou em scripts.
""")

uploaded_files = st.file_uploader("📤 Envie um ou mais arquivos CSV para corrigir", type="csv", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.divider()
        st.subheader(f"📁 Arquivo: {file.name}")

        # Lê as primeiras linhas do arquivo original
        content = file.read().decode('latin1')
        lines = content.splitlines()

        # Remove ponto e vírgula extra ao final das linhas do cabeçalho (primeiras 8 linhas)
        corrected_lines = []
        for i, line in enumerate(lines):
            if i < 8 and line.strip().endswith(';'):
                corrected_lines.append(line.rstrip(';'))
            else:
                corrected_lines.append(line)

        # Junta o conteúdo corrigido
        corrected_content = "\n".join(corrected_lines).encode('latin1')
        corrected_filename = f"corrigido_{file.name}"

        st.success("✅ Cabeçalho corrigido com sucesso!")

        st.download_button(
            label="📥 Baixar arquivo corrigido",
            data=corrected_content,
            file_name=corrected_filename,
            mime='text/csv'
        )
