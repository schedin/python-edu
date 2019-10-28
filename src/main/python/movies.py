#!/usr/bin/env python3

'''
Created on 28 okt. 2019
'''

#def main():
#    movies = {}
    

#if __name__ == "__main__":
#    main()
    
dc_fans = {'peter', 'janne', 'olof'}
marvel_fans = {'conny', 'thomas', 'david', 'lasse', 'janne', 'conny'}

dc_fans.add('donald')

marvel_fans.pop()
#marvel_fans.remove('janne')



print(f'DC = {dc_fans}')
print(f'marvel = {marvel_fans}')
print(f'uni = {dc_fans.union(marvel_fans)}')
print(f'uni = {dc_fans | marvel_fans}')
print(f'int = {dc_fans.intersection(marvel_fans)}')
print(f'diff = {dc_fans.difference(marvel_fans)}')
print(f'symmetric_difference = {dc_fans.symmetric_difference(marvel_fans)}')
