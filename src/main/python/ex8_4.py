#!/usr/bin/env python3

'''
'''

import re

def format_line(line):
    line = line.rstrip()
    
    line = re.sub("'", "''", line)

    #columns = ["'" + c + "'" for c in line.split(",")]    
    #line = ",".join(columns)

    line = ",".join(map(lambda c: "'" + c + "'", line.split(",")))

    
    return line


def main():
    
    
    for line in open("country.txt"):
        line = format_line(line)
        print(line)

if __name__ == "__main__":
    main()
