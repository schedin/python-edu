#!/usr/bin/env python3

'''
'''

import os
import re


def format(line):
    line = line.rstrip()
    
    line = re.sub("'", "''", line)

    columns = ["'" + c + "'" for c in line.split(",")]    
    line = ",".join(columns)
    
    return line

def main():
    
    
    for line in open("country.txt"):
        line = format(line)
        print(line)

if __name__ == "__main__":
    main()
