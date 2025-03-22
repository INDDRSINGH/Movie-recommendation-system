import streamlit as st
import pickle
import requests
import joblib
from sklearn.metrics.pairwise import cosine_similarity

df = pickle.load(open('movies.pkl','rb'))
movies_list = df['original_title']
#cos_sim = pickle.load(open('cos_sim.pkl','rb'))
#cos_sim = joblib.load("cosi_simi.pkl")
vector = joblib.load("vector.pkl")
#cos_sim = cosine_similarity(vector)

def fetch_poster(movie_id):
    url = ("https://api.themoviedb.org/3/movie/{}?api_key="
           "8265bd1679663a7ea12ac168da84d2e8&language=en-US").format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommendation(movie):
    indx = df[df['original_title']==movie].index[0]  #
    vec = vector[indx].reshape(1, -1)
    similarity = cosine_similarity(vec, vector)
    movies = sorted(list(enumerate(similarity.flatten())),reverse=True,key = lambda x:x[1])[1:6]
    # getting top 5 movies with highest similarity score
    movie_name = []
    movie_poster = []
    for i in movies:
        movie_name.append(df.iloc[i[0]].original_title)
        movie_poster.append(fetch_poster(df.iloc[i[0]].id))
    return movie_name , movie_poster

st.title('Movie recommendation system')

selected_movie_name = st.selectbox("Select the Movie you need recommendation for: ",
             movies_list )

if st.button('Recommend'):
    name,poster = recommendation(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(poster[0])
        st.text(name[0])
    with col2:
        st.image(poster[1])
        st.text(name[1])
    with col3:
        st.image(poster[2])
        st.text(name[2])
    with col4:
        st.image(poster[3])
        st.text(name[3])
    with col5:
        st.image(poster[4])
        st.text(name[4])

