import pandas as pd
import streamlit as st


df = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", encoding="latin-1",decimal=",")
df.columns = df.columns.str.replace("\ufeff", "", regex=False).str.strip()



anos_disponiveis = sorted(df["ANO"].unique())
ano_selecionado = st.sidebar.selectbox("Ano de Análise", anos_disponiveis, index=2)

nomeup_disponiveis = ["Taquaril", "Santa Ines"]
nomeup_selecionadas = st.sidebar.multiselect(
    "Bairro:", nomeup_disponiveis, default=nomeup_disponiveis
)

series_disponiveis = ["SERIE HISTORICA"]
series_selecionadas = st.sidebar.multiselect(
    "Serie:", series_disponiveis, default=series_disponiveis
)


df_filtrado = df[(df["ANO"] == ano_selecionado) & (df["NOMEUP"].isin(nomeup_selecionadas) & (df["SERIE"].isin(series_selecionadas)))]