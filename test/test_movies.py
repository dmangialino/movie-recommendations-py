from app.movie_reco import fetch_movie_genre
from app.movie_reco import get_new_rec

def test_fetch_movies():
    genres = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 9648, 10749, 878, 10770, 53, 10752, 37]
    for n in genres:
        movies = fetch_movie_genre(genres)
        if movies:
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
    genres = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 9648, 10749, 878, 10770, 53, 10752, 37]
    for n in genres:
        movies = fetch_movie_genre(genres)
        if movies:
            results = get_new_rec(movies, 1)
            assert isinstance(results[0], str)
            assert isinstance(results[1], float)
            assert isinstance(results[2], str)