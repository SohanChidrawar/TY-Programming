import pickle
import streamlit as st
import requests
import pandas as pd

# Set page configuration and background color
st.set_page_config(page_title="Movie Recommender System", page_icon=":movie_camera:", layout="wide", initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://miro.medium.com/max/5760/1*oRJYoC18Msc4tC6FExYRKQ.jpeg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

# Load movie dataframe and similiarity scores
movies = pd.read_pickle('model/movie_list.pkl')
similarity = pd.read_pickle('model/similarity.pkl')

# Display the dropdown to select a movie
st.write("")
st.subheader("Select a movie from the dropdown")
selected_movie = st.selectbox("", movies['title'].values)

# Display the button to show the recommended movies
st.write("")
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display the recommended movies in a grid of 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], use_column_width=True)
    with col2:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], use_column_width=True)
    with col3:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], use_column_width=True)
    with col4:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], use_column_width=True)
    with col5:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], use_column_width=True)
