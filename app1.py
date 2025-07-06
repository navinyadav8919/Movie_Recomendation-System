import streamlit as st
import pickle
import pandas as pd
import requests

# ✅ Function to fetch poster using TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZjJhOGZkZDY2NjYyMGI2ZTlkZTY5M2NkNzFmNDAzZCIsIm5iZiI6MTc1MTgyNjUwNy43NTgwMDAxLCJzdWIiOiI2ODZhYzA0YmQ0ODlhOWMzMmE1M2ZiMDIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.IeIQ_uE20rZPSUIJel1H4976v6wmbouQMvrkS40PtSg"  # 🔐 Replace with your actual v4 token
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

# ✅ Load movie data
movies_dict = pickle.load(open('D:/Projects/iscale_projects/movie_recomendation_system/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# ✅ Load similarity data
similarity = pickle.load(open('D:/Projects/iscale_projects/movie_recomendation_system/similarity.pkl', 'rb'))

# ✅ Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ✅ Streamlit UI
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Enter the name of a movie', movies['title'].values)

if st.button('recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
