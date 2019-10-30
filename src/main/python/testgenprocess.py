#!/usr/bin/env python3

'''
Created on 30 okt. 2019

@author: Administrator
'''

import sys
import os


os.environ['PATH'] = os.path.dirname(__file__) + os.pathsep + os.environ['PATH']


print(sys.path)

print(os.environ['PATH'])

import getprocs



def main():
    
    print(sys.path)
    
    dir(getprocs)
    

if __name__ == "__main__":
    main()
