#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            d.append(True)
        else:
            d.append(False)
    return (d)
