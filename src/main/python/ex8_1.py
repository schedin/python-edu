#!/usr/bin/env python3

'''
'''


def my_func(value, alist=[]):
    alist.append(value)
    print(alist)
    

def my_func2(value, alist=None):
    if alist is None:
        alist = []
    alist.append(value)
    print(alist)

def main():
    
    my_func("a")
    my_func("b")
    my_func("c")    

    my_func2("a")
    my_func2("b")
    my_func2("c") 

    my_list1 = []
    my_func2("a", my_list1)
    my_func2("b", my_list1)
    my_func2("c", my_list1) 


    my_list2 = []
    my_func2("a", my_list2)
    my_func2("b", my_list2)



if __name__ == "__main__":
    main()
