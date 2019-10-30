#!/usr/bin/env python3

'''
'''

import decimal

def frange(start, stop=None, step=0.25):
    if not step:
        return # TODO throw exception
    
    if stop is None:
        stop = start
        start = 0
    
    

    
    next_ = decimal.Decimal(str(start))
    step = decimal.Decimal(str(step))
    while next_ < stop:
        yield float(next_)
        next_ += step


def main():
    print(list(frange(1.1, 3)))
    print(list(frange(1, 3, 0.33)))
    print(list(frange(1, 3, 1)))  # Should print [1.0, 2.0]
    print(list(frange(3, 1)))     # Should print empty list
    print(list(frange(1, 3, 0)))  # Should print empty list
    print(list(frange(-1, -0.5, 0.1)))
    
    for num in frange(3.142, 12):
        print(f"{num:05.2f}")
        
    print(frange(1, 2))
    

if __name__ == "__main__":
    main()
