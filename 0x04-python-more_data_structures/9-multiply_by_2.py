#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    new_dict = a_dictionary.copy()
    for i in new_dict.keys():
        new_dict[i] *= 2
    return new_dict
