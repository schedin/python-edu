#!/usr/bin/env python3

'''
'''

def say_hello(greeting, recipiet="everyone"):
    message = greeting + " " + recipiet
    print(message)


def main():
    say_hello("Hello", "Sweden")
    say_hello("Good morning", "Unitied Kingdom")
    say_hello("Hi")


if __name__ == "__main__":
    main()
