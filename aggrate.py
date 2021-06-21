import pandas as pd

dfr = pd.read_csv('ratingscut.csv', delimiter=',')
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

print(ratings)