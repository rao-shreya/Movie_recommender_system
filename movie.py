import streamlit as st
import pandas as pd
from model import recommend



st.title('Movie Recommender System')

# Sample music dataset (replace this with your actual data)
df = pd.read_csv('tmdb_5000_movies.csv')

selected_movie = st.selectbox('Select a movie:', df['original_title'])

if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie)
    st.write(recommendations)
