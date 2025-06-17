import sys
import pandas as pd
import streamlit as st
import json

sys.path.append("/home/vitor/Documentos/Projetos/projetos_conjunto/")
from src.validacion import validacion_format  # noqa: E402

st.set_page_config(page_title="Preenchendo os dados")

st.write("## Inseria os dados necessarios para as analisis")

path_oot = st.text_input("Adicione o path do oot .parquet")
if path_oot and validacion_format(path_oot, ".parquet"):
    st.dataframe(pd.read_parquet(path_oot).head())
elif path_oot:
    st.error("Formato ou caminho invalido")

path_vars = st.text_input("Adicione o path das variaveis .json")
if path_vars and validacion_format(path_vars, ".json"):
    st.json(json.load(open(path_vars, "r")))
elif path_vars:
    st.error("Formato ou caminho invalido")

path_pickle = st.text_input("Adicione o path do arquivo .pickle")
