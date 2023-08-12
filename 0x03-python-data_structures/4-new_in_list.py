#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    replace = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(idx):
            replace[idx] = element
        return replace
