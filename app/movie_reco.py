from imdb import IMDb

ia = IMDb()

#print(dir(ia))

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)
