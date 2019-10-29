#!/usr/bin/env python3

'''

'''
import re

def main():
    words = [w.rstrip() for w in open(r'words').readlines()]
    
    p = re.compile(r'^(.)(.).\2\1$')
    
    for word in words:
        m =  p.search(word)
        if m:
            print(f"Matched {m.group()} in {word}")
            print("Group: " + str(m.group()))
            print("Groups: " + str(m.groups()))
            print(word)


if __name__ == "__main__":
    main()
