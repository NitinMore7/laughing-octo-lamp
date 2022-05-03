import pickle
import streamlit as st
import pandas as pd
import requests


api_key = 'f77fbc0c75c8329568d7fc4e7e2254cb'
def Fetch_poster(movie_id,key):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}',movie_id,key)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Choose from the list pf movies',movies['title'].values)
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distance = similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)),reverse = True,key = lambda x:x[1])[1:6]
  ans = []
  ans_poster= []
  for i in movies_list:
    ans.append(movies.iloc[i[0]].title)
    ans_poster.append(Fetch_poster(i[0],api_key))
  return ans,ans_poster


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      names,poster = recommend(i)
