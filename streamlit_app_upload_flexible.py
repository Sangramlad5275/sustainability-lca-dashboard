
import streamlit as st
import pandas as pd

st.sidebar.header("Upload Your Data File")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=None)

def read_uploaded_file(file):
    name = file.name.lower()
    if name.endswith(".csv"):
        return pd.read_csv(file)
    elif name.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)
    elif name.endswith(".json"):
        return pd.read_json(file)
    elif name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif name.endswith(".xml"):
        return file.read().decode("utf-8")
    else:
        return None

if uploaded_file is not None:
    try:
        result = read_uploaded_file(uploaded_file)
        if isinstance(result, pd.DataFrame):
            st.success(f"File '{uploaded_file.name}' uploaded and parsed as DataFrame!")
            df = result
        elif isinstance(result, str):
            st.success(f"File '{uploaded_file.name}' uploaded as text!")
            st.text_area("File Content", result, height=300)
            st.stop()
        else:
            st.error("Unsupported file type. Please upload a CSV, Excel, JSON, TXT, or XML file.")
            st.stop()
    except Exception as e:
        st.error(f"Failed to read the uploaded file: {e}")
        st.stop()
else:
    st.warning("Please upload a data file to proceed.")
    st.stop()


import streamlit as st
from overview import show_overview

st.set_page_config(page_title="LCA Dashboard", layout="wide")
st.sidebar.title("LCA Navigation")
tab = st.sidebar.radio("Choose view", ["LCA Overview"])

if tab == "LCA Overview":
    show_overview()
