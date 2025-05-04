
import streamlit as st
import pandas as pd
import io

st.title("🔧 Corrigir arquivos INMET para formato compatível")

uploaded_files = st.file_uploader(
    "📂 Envie os arquivos INMET (qualquer formato)", accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"📥 Processando: {uploaded_file.name}")

        # Detecta se é CSV ou Excel
        file_suffix = Path(uploaded_file.name).suffix.lower()

        try:
            if file_suffix == ".csv":
                df = pd.read_csv(uploaded_file, sep=';', encoding='latin1', skip_blank_lines=True)
            elif file_suffix in [".xls", ".xlsx"]:
                df = pd.read_excel(uploaded_file)
            else:
                st.warning(f"❌ Formato não reconhecido: {uploaded_file.name}")
                continue

            # Substituir vírgula por ponto em todas as colunas numéricas
            df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)

            # Gerar novo arquivo CSV corrigido
            output_name = uploaded_file.name.replace(" ", "_").replace(".CSV", "") + "_corrigido.csv"
            df.to_csv(output_name, index=False)
            with open(output_name, "rb") as f:
                st.download_button(
                    label=f"⬇️ Baixar arquivo corrigido: {output_name}",
                    data=f,
                    file_name=output_name,
                    mime="text/csv"
                )

        except Exception as e:
            st.error(f"Erro ao processar {uploaded_file.name}: {e}")
