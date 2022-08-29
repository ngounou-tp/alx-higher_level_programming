#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    while i < len(my_list):
        print("{}".format(my_list[i]))
        i = i + 1
a = [1, 2, 2,3]
print_list_integer(a)
   