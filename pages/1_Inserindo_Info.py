import sys
import pandas as pd
import streamlit as st
import json

sys.path.append("/home/vitor/Documentos/Projetos/projetos_conjunto/")
from src.validacion import validacion_format  # noqa: E402

st.set_page_config(page_title="Preenchendo os dados")

st.write("## Inseria os dados necessarios para as analisis")

with st.form(key="formulario", clear_on_submit=False):
    path_oot = st.text_input("Adicione o path do oot .parquet")
    if path_oot and validacion_format(path_oot, ".parquet"):
        df_oot = pd.read_parquet(path_oot)
        st.dataframe(df_oot.head())
    elif path_oot:
        st.error("Formato ou caminho invalido")

    path_vars = st.text_input("Adicione o path das variaveis .json")
    if path_vars and validacion_format(path_vars, ".json"):
        st.json(json.load(open(path_vars, "r")))
    elif path_vars:
        st.error("Formato ou caminho invalido")

    path_pickle = st.text_input("Adicione o path do arquivo .pickle")
    if path_pickle and validacion_format(path_pickle, ".pickle"):
        pass
    elif path_pickle:
        st.error("Formato ou caminho invalido")

    click_enviar = st.form_submit_button("Enviar")


if (
    click_enviar
    and path_oot
    and validacion_format(path_oot, ".parquet")
    and path_vars
    and validacion_format(path_vars, ".json")
    and path_pickle
    and validacion_format(path_pickle, ".pickle")
):
    st.session_state["path_oot"] = path_oot
    st.session_state["path_vars"] = path_vars
    st.session_state["path_pickle"] = path_pickle
    st.success("Dados salvos! Agora vá para a página de processamento.")
elif click_enviar:
    st.error("Formato ou caminho invalido")
