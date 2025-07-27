
import streamlit as st
from overview import show_overview

st.set_page_config(page_title="LCA Dashboard", layout="wide")
st.sidebar.title("LCA Navigation")
tab = st.sidebar.radio("Choose view", ["LCA Overview"])

if tab == "LCA Overview":
    show_overview()
