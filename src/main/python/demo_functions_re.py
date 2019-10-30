#!/usr/bin/env python3

'''
'''

import re
import cProfile


def search_pattern(pattern:str, filename=r'words') -> int:
    print(f"Annotations = {search_pattern.__annotations__}")
    
    count_lines = 0
    with open(filename) as fh:
        #pattern = re.compile(pattern)
        for line in fh:
            #m = pattern.search(line)
            m = re.search(pattern, line)
            if m:
                print(f"Matched {m.group()} in {line}", end="")
                count_lines += 1
            
    return count_lines


def main():
    cProfile.run("search_pattern(r'^.{23}')", "reprof.stat")
    
    
    #print(search_pattern(r'^.{23}'))
    #print(search_pattern(r'^(.)(.)(.).\3\2\1'))
    

if __name__ == "__main__":
    
    #cProfile.run("main")
    
    main()
