#!/usr/bin/env python3

'''
'''

movies = {'olof': ['braveheart', 'frozen', 'tangled'],
          'josefine': 'pride & prejudice',
          'jorgen': 'godfather',
          'thomas': ['the right stuff'],
          'lasse': 'spice girls'}


import pprint
import copy


def main():
    
    #copy_movies = movies.copy()
    copy_movies = copy.deepcopy(movies)
    
    #pprint.pprint(movies)
    #pprint.pprint(copy_movies)
    
    copy_movies['thomas'][0] = 'Alien'

    pprint.pprint(movies)
    print("########")
    pprint.pprint(copy_movies)


if __name__ == "__main__":
    main()

