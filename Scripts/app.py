import pandas as pd
import streamlit as st
import requests
from dotenv import load_dotenv,find_dotenv
import os

env_file=find_dotenv('.env')
load_dotenv(env_file)

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.environ.get("TMDB_API_KEY")}&language=en-US')
    data=response.json()
    return "https://image.tmdb.org/t/p/w500" + data.get('poster_path')

st.set_page_config(page_title='Movie Recommendation System', page_icon='🎬', initial_sidebar_state='auto')
st.title('Movie Recommendation System')

with open('movies.pkl', 'rb') as f:
    movies_df = pd.read_pickle(f)
    
with open('similarity.pkl', 'rb') as f:
    similarity = pd.read_pickle(f)
    
def movie_recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_df.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_posters

movie_title = st.selectbox('Select a movie:', movies_df['title'].values)

if st.button('Recommend'):
    movie,poster=movie_recommend(movie_title)
    col1,col2,col3,col4,col5=st.columns(5)
    
    columns=[col1,col2,col3,col4,col5]
    for idx,col in enumerate(columns):
        with col:
            st.image(poster[idx])
            st.text(movie[idx])


