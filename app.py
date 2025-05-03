
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Corretor de CSV", layout="centered")

st.title("🛠️ Corretor de Arquivos CSV para Streamlit")

st.write("""
Este aplicativo corrige arquivos `.csv` que estão com formato ou codificação incorreta.
Ele reescreve os arquivos com codificação UTF-8 e salva novamente como `.csv` legível para outros apps Streamlit.
""")

uploaded_files = st.file_uploader("📁 Envie um ou mais arquivos CSV para corrigir:", accept_multiple_files=True, type=["csv"])

if uploaded_files:
    for file in uploaded_files:
        st.markdown(f"### 🔍 Processando: `{file.name}`")

        try:
            # Lê usando Latin-1 para garantir compatibilidade
            df = pd.read_csv(file, sep=';', encoding='latin1', engine='python')

            # Cria buffer para salvar o arquivo corrigido
            buffer = io.BytesIO()
            df.to_csv(buffer, index=False, sep=';', encoding='utf-8-sig')
            buffer.seek(0)

            nome_corrigido = file.name.replace(" ", "_").replace(".CSV", "").replace(".csv", "") + "_corrigido.csv"
            st.download_button(
                label="⬇️ Baixar arquivo corrigido",
                data=buffer,
                file_name=nome_corrigido,
                mime="text/csv"
            )
            st.success(f"Arquivo `{nome_corrigido}` corrigido com sucesso!")

        except Exception as e:
            st.error(f"Erro ao processar `{file.name}`: {e}")
