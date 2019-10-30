#!/usr/bin/env python3

'''
'''

def frange(start, stop, step=0.25):
    if not step:
        return # TODO throw exception
    
    next_ = start
    while next_ < stop:
        yield next_
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
