import pickle
import streamlit as st 
import requests
import pandas as pd

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=6f3cc9bbb4f3a974f98696c05ad2c917&language=en-US".format(movie_id)
    data= requests.get(url)
    data=data.json()
    print(data)
    if 'poster_path' in data:
        poster_path=data['poster_path']
        full_path="https://image.tmdb.org/t/p/w500/" + poster_path
        print(full_path)
        return full_path
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Image+Available"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies_name=[]
    recommended_movie_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movie_poster

st.header("Movie Recommender System") 
movies=pickle.load(open('Artifacts/movie_list.pkl','rb'))
similarity=pickle.load(open('Artifacts/similarity.pkl','rb'))

movies_list = movies['title'].values
selected_movies=st.selectbox(
    'Type or Select a movie for recommendation',
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movies_name , recommended_movie_poster= recommend(selected_movies)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movie_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movie_poster[2])

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movie_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movie_poster[4])

    