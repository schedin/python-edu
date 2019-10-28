#!/usr/bin/env python3

'''

'''
import re

def main():
    words = [w.rstrip() for w in open(r'words').readlines()]
    
    for word in words:
        m = re.search(r'^..............', word)
        if m:
            print(word)


if __name__ == "__main__":
    main()
