#!/usr/bin/env python3
# coding=utf-8

'''
'''

import sys

def say_hello(greeting="Awright", recipiet="everyone"):
    message = greeting + " " + recipiet
    print(message, sep=" ", end="\n", file=sys.stdout)


def main():
    say_hello("Hello", "Sweden")
    say_hello(greeting="Good morning", recipiet="Unitied Kingdom")
    say_hello(recipiet="kompis", greeting="Läget")
    say_hello("Good evning", recipiet="Stockholm")
    say_hello("Hi")
    say_hello()


if __name__ == "__main__":
    main()
