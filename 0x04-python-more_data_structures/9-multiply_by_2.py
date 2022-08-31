#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k,v in a_dictionary.items():
        a_dictionary[k] = v * v
    return a_dictionary
