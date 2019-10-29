#!/usr/bin/env python3

'''

'''


import re

def main():
    
    index = {}
    
    with open(r'messier.txt', 'r') as fh:
        for line in fh:
            
            startIndex = fh.tell() - len(line)
            
            if re.match(r'^M', line):
                print(line)
                print(startIndex)


if __name__ == "__main__":
    main()

