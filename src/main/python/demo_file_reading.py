#!/usr/bin/env python3

'''

'''

import os
import sys

def main():
    pythonfileDir = os.path.dirname(__file__)
    #filename = os.path.normpath(pythonfileDir + r'/../resources/movies.txt')
    filename = r'wsords'
    try:
        with open(filename, encoding='utf_8') as fh:
            for line in fh:
                line = line.strip()
                print(line)
    except FileNotFoundError as e:
        print(e.filename)
        print(f"Could not open file: {str(e)}", file=sys.stderr)
        print(sys.exc_info())
        
        sys.exit(1)
    
    




if __name__ == "__main__":
    main()
