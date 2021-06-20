from imdb import IMDb

ia = IMDb()

#print(dir(ia))

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)


movie = ia.get_movie('0133093')
movie.infoset2keys
{'main': ['cast', 'genres', ..., 'top 250 rank'], 'plot': ['plot', 'synopsis']}
movie = ia.get_movie('0094226', info=['taglines', 'plot'])
movie.infoset2keys
{'taglines': ['taglines'], 'plot': ['plot', 'synopsis']}
movie.get('title')
movie.get('taglines')[0]
'The Chicago Dream is that big'