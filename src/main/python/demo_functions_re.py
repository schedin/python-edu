#!/usr/bin/env python3

'''
'''

import re

def search_pattern(pattern, filename=r'words'):
    count_lines = 0
    with open(filename) as fh:
        pattern = re.compile(pattern)
        for line in fh:
            m = pattern.search(line)
            if m:
                print(f"Matched {m.group()} in {line}", end="")
                count_lines += 1
            
    return count_lines


def main():
    print(search_pattern(r'^.{23}'))
    print(search_pattern(r'^(.)(.)(.).\3\2\1'))
    

if __name__ == "__main__":
    main()
