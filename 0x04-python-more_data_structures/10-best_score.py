#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    new_dict = -100
    str = ""
    for i, j in a_dictionary.items():
        if (j > new_dict):
            str = i
            new_dict = j
    return str
