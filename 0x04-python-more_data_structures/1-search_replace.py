#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for item in new_list:
        if item == search:
            new_list[new_list.index(item)] = replace
    return new_list
