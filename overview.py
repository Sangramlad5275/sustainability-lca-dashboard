
import streamlit as st
import pandas as pd
import plotly.express as px

def show_overview():
    st.title("🌍 Sustainability LCA Overview")

    df = pd.read_csv("lca_sample.csv")
    st.dataframe(df)

    st.subheader("CO₂ Emissions by Lifecycle Stage")
    fig = px.bar(df, x="Stage", y="CO2_Emissions_kg", text="CO2_Emissions_kg")
    st.plotly_chart(fig)

    st.subheader("Energy Use by Stage")
    fig2 = px.pie(df, names="Stage", values="Energy_MJ")
    st.plotly_chart(fig2)

    st.subheader("Water Usage by Stage")
    fig3 = px.line(df, x="Stage", y="Water_Liters", markers=True)
    st.plotly_chart(fig3)
