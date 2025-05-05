import streamlit as st
import pandas as pd
import io
import zipfile
import os

st.set_page_config(page_title="Conversor de Extensão para CSV", layout="centered")
st.title("📁 Conversor de Arquivos para .CSV")
st.markdown("Faça upload de até **15 arquivos** `.csv`, `.xls` ou `.xlsx`. O conteúdo será mantido e convertido para `.csv`.")

uploaded_files = st.file_uploader("Envie os arquivos", type=["csv", "xls", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    os.makedirs("convertidos", exist_ok=True)

    for uploaded_file in uploaded_files:
        try:
            filename = uploaded_file.name
            base_name = os.path.splitext(filename)[0]
            ext = filename.split(".")[-1].lower()
            output_path = f"convertidos/{base_name}.csv"

            if ext == "csv":
                with open(output_path, "wb") as f:
                    f.write(uploaded_file.read())
            elif ext in ["xls", "xlsx"]:
                df = pd.read_excel(uploaded_file)
                df.to_csv(output_path, index=False, sep=";", encoding="utf-8")
            else:
                st.error(f"❌ Tipo de arquivo não suportado: {filename}")
                continue

            st.success(f"✅ {filename} convertido com sucesso.")

        except Exception as e:
            st.error(f"❌ Erro ao processar {filename}: {e}")

    # Compactar
    with zipfile.ZipFile("convertidos.zip", "w") as zipf:
        for root, _, files in os.walk("convertidos"):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

    with open("convertidos.zip", "rb") as f:
        st.download_button("📦 Baixar Arquivos Convertidos (.zip)", f, file_name="convertidos.zip")