#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [list(map(lambda x: x * x, position)) for position in matrix]
    return square
