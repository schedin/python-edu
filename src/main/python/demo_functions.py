#!/usr/bin/env python3

'''
'''

def say_hello(greeting="Awright", recipiet="everyone"):
    message = greeting + " " + recipiet
    print(message)


def main():
    say_hello("Hello", "Sweden")
    say_hello("Good morning", "Unitied Kingdom")
    say_hello("Hi")
    say_hello()


if __name__ == "__main__":
    main()
