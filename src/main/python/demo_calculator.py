#!/usr/bin/env python3

'''
Simulate a calculator program
'''

def multiply(x, z):
    return x * z


def add(x, z):
    return x + z


def divide(x, z):
    return float(x/z)


def main():
    print(f"3 * 4 is {multiply(3, 4)}")
    print(f"3 + 4 is {add(3, 4)}")
    print(f"4 / 3 is {divide(4, 3)}")
    

if __name__ == "__main__":
    main()
