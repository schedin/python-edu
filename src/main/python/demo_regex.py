#!/usr/bin/env python3

'''

'''
import re

def main():
    words = [w.rstrip() for w in open(r'words').readlines()]
    
    for word in words:
        m = re.search(r'^..............', word)
        m = re.search(r'^(.)(.).\2\1$', word)
        m = re.search(r'([A-Z]).*\1$', word)
        if m:
            print("Group: " + str(m.group()))
            print("Groups: " + str(m.groups()))
            print(word)


if __name__ == "__main__":
    main()
