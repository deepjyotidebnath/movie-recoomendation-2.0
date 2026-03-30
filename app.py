import streamlit as st

from recommender import recommend, movie_similarity_df

st.title("🎬Netflix Movie Recommendation System")

movie_list = movie_similarity_df.columns


selected_movie = st.selectbox(
    "select a movie",
    movie_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.write("### Recommended Movies")

    for movie in recommendations:
        st.write(movie)