#!/usr/bin/env python3

'''

'''
movies = {'olof': 'braveheart',
          'josefine': 'pride & prejudice',
          'jorgen': 'godfather',
          'thomas': 'the right stuff',
          'lasse': 'spice girls'}

print(movies)
print(movies.keys())
print(movies.values())



print('######## keys() ##########')
for name in movies.keys():
    #print(name + str(movies[name]), end='\n\n')
    print(f'name = {name}, movie = {movies[name]}')

print('######## values() ##########')
for movie in movies.values():
    print(movie)

print('######## items() ##########')
for name, movie in movies.items():
    print(movie)
    print(name)

  
