#!/usr/bin/env python3

'''
'''

import os

start_cpu_time = 0


def start_timer():
    '''Start the timer'''
    
    global start_cpu_time
    times = os.times()
    start_cpu_time =  times[0] + times[1]
    

def end_timer():
    '''Stop the timer and print the result'''
    
    global start_cpu_time
    times = os.times()
    end_cpu_time =  times[0] + times[1]
    elapsed_time = end_cpu_time - start_cpu_time
    print(f'Elapsed time: {elapsed_time:12.3}')


def main():
    start_timer()
    count = 0
    for row in open("words"):
        count += len(row)

    end_timer()
    
    print("Number of chars: ", count)


if __name__ == "__main__":
    main()
