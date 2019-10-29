#!/usr/bin/env python3

'''
'''
def main():
    
    files = []
    
    for x in range(0, 100000):
        with open(r'foo.txt', 'rt') as fh:
            files.append(fh)
    
    print(len(files))
    

if __name__ == "__main__":
    main()
