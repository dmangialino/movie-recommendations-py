from app.movie_reco import fetch_movie_genre


from app.movie_reco import fetch_movie_genre

def test_fetch_movies():
    movies = fetch_movie_genre(28)
    assert isinstance(movies, list)
    movie = movies[0]
    assert isinstance(movie, dict)
    # vote = movies[0]["vote_average"]
    for mov in movies:
        assert "vote_average" in list(mov.keys())

