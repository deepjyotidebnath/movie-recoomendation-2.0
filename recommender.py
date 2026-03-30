import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

data = pd.merge(ratings, movies, on="movieId")

movie_matrix= data.pivot_table(
    index='userId',
    columns='title',
    values='rating'
).fillna(0)

movie_similarity = cosine_similarity(movie_matrix.T)

movie_similarity_df = pd.DataFrame(
    movie_similarity,
    index=movie_matrix.columns,
    columns=movie_matrix.columns
)

def recommend(movie_name, n=5):
    if movie_name not in movie_similarity_df.columns:
        return["Movie not found"]
    

    similar_movies = movie_similarity_df[movie_name]\
        .sort_values(ascending=False)[1:n+1]
    
    return list(similar_movies.index)

print(recommend("Inception"))
