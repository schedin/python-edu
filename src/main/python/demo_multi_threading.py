#!/usr/bin/env python3

import threading
import time


def cycle_race(*args):
    cyclist = args[0]
    handicap = args[1]
    
    for distance in range(0, 1001, 100):
        print(f"{cyclist} - {distance}m")
        time.sleep(handicap)
    return

print("Starting cycle race.")

t1 = threading.Thread(target=cycle_race, args=('david', 1.345))
t2 = threading.Thread(target=cycle_race, args=('conny', 1.567))

t1.start()
t2.start()

t1.join()
t2.join()


print("Race finished.")
