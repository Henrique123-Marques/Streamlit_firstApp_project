import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

df_reviews = pd.read_csv("C:\Projects\Python\Data\AsimovAcademy_IntroducaoAoPython\Streamlit_firstApp_project\dataset\customer reviews.csv")
df_top100_books = pd.read_csv("C:\Projects\Python\Data\AsimovAcademy_IntroducaoAoPython\Streamlit_firstApp_project\dataset\Top-100 Trending Books.csv")

preco_max = df_top100_books["book price"].max()
preco_min = df_top100_books["book price"].min()

max_preco = st.sidebar.slider("Price Range", preco_min, preco_max, preco_max)
df_books = df_top100_books[df_top100_books['book price'] <= max_preco]
df_books

#Grafico de Anos de Publicacao
figura = px.bar(df_books["year of publication"].value_counts())
figura2 = px.histogram(df_books["book price"])

coluna1, coluna2 = st.columns(2)
coluna1.plotly_chart(figura)
coluna2.plotly_chart(figura2)
