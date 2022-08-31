#!/usr/bin/python3
def uniq_add(my_list=[]):
    m = set(my_list)
    n = list(m)
    sum = 0
    for i in n:
        sum = sum + i
    return sum

    