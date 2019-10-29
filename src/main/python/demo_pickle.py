#!/usr/bin/env python3

'''
'''

import pickle
import pprint


def main():
    
    movies = {
        'olof': ['braveheart', 'frozen', 'tangled'],
        'josefine': ['cars', 'emma'],
        'lasse': ['memento'],
        'thomas': [],        
        }
    
    fh_out = open(r'movies.p', "wb")
    pickle.dump(movies, fh_out, protocol=4)
    fh_out.close()
    
    fh_in = open(r'movies.p', "rb")
    copy_movies = pickle.load(fh_in)
    pprint.pprint(copy_movies)
    fh_in.close()
    
    pprint.pprint(f'josefine second movie is {movies["josefine"][1]}')
    
    
if __name__ == "__main__":
    main()
