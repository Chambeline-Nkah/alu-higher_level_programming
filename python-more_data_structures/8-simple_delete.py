#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
     new_dict = dict(a_dictionary)
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return new_dict
