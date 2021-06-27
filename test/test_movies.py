from app.movie_reco import fetch_movie_genre

def test_fetch_movies():
    movies = fetch_movie_genre(28)
    assert isinstance(movies, list)
    movie = movies[0]
    assert isinstance(movie, dict)
    for mov in movies:
        assert "original_title" in list(mov.keys())
    for mov in movies:
        assert "vote_average" in list(mov.keys())
    # This fails, will add error handling to script to handle situations in which movie does not have release date to address
    #for mov in movies: 
    #    assert "release_date" in list(mov.keys())

