import pickle
import streamlit as st
import pandas as pd
import requests

def Fetch_poster(movie_id,key):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, key))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distance = similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)),reverse = True,key = lambda x:x[1])[1:6]
  ans = []
  ans_poster= []
  for i in movies_list:
    ans.append(movies.iloc[i[0]].title)
    ans_poster.append(Fetch_poster(movies.iloc[i[0]].movie_id,api_key))
  return ans,ans_poster


api_key = 'f77fbc0c75c8329568d7fc4e7e2254cb'
movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Choose from the list of movies',movies['title'].values)
similarity = pickle.load(open('similarity.pkl','rb'))



if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])