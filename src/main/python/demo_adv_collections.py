#!/usr/bin/env python3

'''
'''

students = [
    'olof',
    'peter',
    'david',
    'lennart',
    'kenneth',
    'joakim',
    'jorgen',
    'josefine',
    'lasse',    
    'janne',
]

def f1():
    wee_names = []
    for name in students:
        if len(name) <= 5:
            wee_names.append(name)
    
    
    print(f"1. Short names = {wee_names}")


def f2():
    def filter_names(name):
        return len(name) <= 5
    
    
    wee_names = []
    for name in students:
        if filter_names(name):
            wee_names.append(name)
    
    print(f"2. Short names = {wee_names}")


def f3():
    def filter_names(name):
        return len(name) <= 5
        
    wee_names = list(filter(filter_names, students))
    print(f"3. Short names = {wee_names}")


def f4():
    wee_names = list(filter(lambda n: len(n) <=5, students))
    print(f"4. Short names = {wee_names}")

def f5():
    wee_names = [name for name in students if len(name) <=5]
    print(f"5. Short names = {wee_names}")


f1()
f2()
f3()
f4()
f5()