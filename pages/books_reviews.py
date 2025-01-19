import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

df_reviews = pd.read_csv("C:\Projects\Python\Data\AsimovAcademy_IntroducaoAoPython\Streamlit_firstApp_project\dataset\customer reviews.csv")
df_top100_books = pd.read_csv("C:\Projects\Python\Data\AsimovAcademy_IntroducaoAoPython\Streamlit_firstApp_project\dataset\Top-100 Trending Books.csv")

#Caixa de selecao dos livros no sidebar
books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

#Selecao de reviews do livro baseado na seleçao no sidebar
df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

#Informacoes do livro
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

#Dados do livro
st.title(book_title)
st.subheader(book_genre)
coluna1, coluna2, coluna3 = st.columns(3)
coluna1.metric("Price", book_price)
coluna2.metric("Rating", book_rating)
coluna3.metric("Year of Publication", book_year)

st.divider()

#Descricao do livro
for row in df_reviews_f.values:
	message = st.chat_message(f"{row[4]}")
	message.write(f"**{row[2]}**")
	message.write(row[5])



