import pandas as pd


dfr = pd.read_csv('ratings.csv', delimiter=',')
list_of_rating = [list(row) for row in dfr.values]
# list_of_rating = [int(n[0]) for n in list_of_ratings]
# print(list_of_rating)

ratings  = {}
for n in list_of_rating:
    if str(int(n[1])) not in ratings.keys():
        ratings.update({str(int(n[1])): [n[2],1]})
    elif str(int(n[1])) in ratings.keys():
        ratings[str(int(n[1]))][0]+= n[2]
        ratings[str(int(n[1]))][1]+= 1


for n in ratings:
    ratings[n][0] = ratings[n][0]/ratings[n][1]

# Create a dataframe from csv
dfm = pd.read_csv('movies.csv', delimiter=',')
# User list comprehension to create a list of lists from Dataframe rows
list_of_movies = [list(row) for row in dfm.values]

for n in list_of_movies:
    if str(n[0]) in ratings.keys():
        n.append(ratings[str(n[0])][0])
    else:
        n.append(6)

# print(list_of_movies)

genre = input('Please enter a genre ').capitalize()

selected = []
for n in list_of_movies:
    if genre in n[2]:
        selected.append(n)

from operator import itemgetter

selected.sort(reverse=True, key=itemgetter(3))
dfm = pd.read_csv('movies.csv', delimiter=',')


for n in selected:
    if n[3] > 4.5:
        print(n)