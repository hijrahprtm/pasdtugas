import streamlit as st
import pandas as pd

# Input file excel
df = pd.read_excel("pasdtubes.xlsx")

# Judul App
st.title("MovieFinder")

# Menampilkan Data dalam tabel
st.write("Data from XLSX file:")
st.write(df)

# Fitur Pencarian
st.subheader("Search Movies")
search_term = st.text_input("Enter movie title:")

# Filter berdasarkan judul film
if search_term:
    search_result = df[df["title"].str.contains(search_term, case=False, na=False)]
    st.write(search_result)
else:
    st.write("Enter a movie title to search.")

# Fitur Pencarian berdasarkan genre
st.subheader("Search Movies by Genre")
selected_genre = st.selectbox("Select a genre:", df['genres'].unique())
filtered_movies = df[df['genres'] == selected_genre]

if not filtered_movies.empty:
    movie_titles = filtered_movies['title'].tolist()
    st.write("Movies in the selected genre:")
    st.write(movie_titles)
else:
    st.write("No movies found in the selected genre.")
