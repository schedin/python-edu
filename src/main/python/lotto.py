#!/usr/bin/env python3

'''
Created on 28 okt. 2019

@author: Administrator
'''
import random

lotto = set()

while len(lotto) < 6:
    lotto.add(random.randint(1, 50))
    
print(lotto)
print(f'Lottery numbers = {lotto}')
