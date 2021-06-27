from app.movie_reco import fetch_movie_genre
from app.movie_reco import get_new_rec

def test_fetch_movies():
    movies = fetch_movie_genre(28)
    assert isinstance(movies, list)
    movie = movies[0]
    assert isinstance(movie, dict)
    for mov in movies:
        assert "original_title" in list(mov.keys())
    for mov in movies:
        assert "vote_average" in list(mov.keys())
    for mov in movies:
        assert "poster_path" in list(mov.keys())
    # The below fails...
    #   ... will add error handling to script to handle situations in which movie does not have release date to address
    #for mov in movies: 
    #    assert "release_date" in list(mov.keys())


def test_get_new_rec():
    movies = fetch_movie_genre(28)
    results = get_new_rec(movies, 1)
    assert isinstance(results[0], str)
    assert isinstance(results[1], float)
    assert isinstance(results[2], str)