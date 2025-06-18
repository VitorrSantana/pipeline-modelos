import streamlit as st

# from src.config import PATH_OOT,PATH_PICKLE,PATH_VARS

if "path_oot" in st.session_state:
    st.write(st.session_state["path_oot"])
