import streamlit as st


def show_header():
    st.title("🤖 Analisis Modelo")
    st.markdown("---")


def intro():

    st.write("## Bem vindo ao analisador de Estabilidade de Modelos 👋🚀")
    st.markdown(
        """
        ### Esse analisador vai permitir que voce compartilhe algumas informações 📝:
        -   **Modelo**   : Arquivo ```.pickle``` do modelo
        -   **OOT**      : Arquivo ```.parquet``` onde contém o dataframe de validação do Modelo
        -   **variaveis**: Arquivo ```.json``` contem variaveis numericas e categoricas
        ### Após essas informações fornecidas voce podera simular:
        -   Impacto ao levar uma o mais variaveis para nullo ou constante 📊
        -   Migração do score predito ao fazer essa alteração 📈
    """  # noqa: E501
    )
    st.markdown(
        """
        ### Se ligue no formato padrão para as entradas com os exemplos abaixo 💡:
    """  # noqa: E501
    )
