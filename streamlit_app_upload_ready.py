
import streamlit as st
import pandas as pd

st.sidebar.header("Upload Excel File")
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
else:
    st.warning("Please upload an Excel file to proceed.")
    st.stop()


import streamlit as st
from overview import show_overview

st.set_page_config(page_title="LCA Dashboard", layout="wide")
st.sidebar.title("LCA Navigation")
tab = st.sidebar.radio("Choose view", ["LCA Overview"])

if tab == "LCA Overview":
    show_overview()
