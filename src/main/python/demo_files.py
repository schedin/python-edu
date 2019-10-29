#!/usr/bin/env python3

'''
'''

movies = "A list of movies..."

import os

def main():
    
    pythonfileDir = os.path.dirname(__file__)
    
    filename = os.path.normpath(pythonfileDir + r'/../../../target/movies.txt')
    
    target_dir = os.path.dirname(filename)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    
    with open(filename, 'w') as fh:
        fh.write(f"{movies}")


    with open(filename) as fh:
        print(fh.read())

    

if __name__ == "__main__":
    main()
