#!/usr/bin/env python3

'''

'''


def get_numbers():
    '''Generate and return a list of numbers'''
    print("Executing get_numbers()")
    
    numbers = []
    for x in range(10):
        numbers.append(x)
    
    return numbers


def generate_numbers():
    print("Executing generate_numbers()")
    
    for x in range(10):
        yield x
    

def main():
    for z in get_numbers():
        print(z)
    

    for z in generate_numbers():
        print(z)

if __name__ == "__main__":
    main()
