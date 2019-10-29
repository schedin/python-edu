#!/usr/bin/env python3

'''

'''

import os

def main():
    pythonfileDir = os.path.dirname(__file__)
    #filename = os.path.normpath(pythonfileDir + r'/../resources/movies.txt')
    filename = r'words'
    
    with open(filename, encoding='utf_8') as fh:
        for line in fh:
            line = line.strip()
            print(line)
    




if __name__ == "__main__":
    main()
