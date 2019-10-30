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

cycle_race('david', 1.345)
cycle_race('conny', 1.567)

print("Race finished.")
