#!/usr/bin/env python3
import math

def empty(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(0)
    return (matrix)

def matrix_prod(s_matrix, k_matrix, cols, argv):
    one = check_float(argv, cols)
    r_matrix = [[0 for i in range(cols)] for i in range(math.trunc(len(argv[1]) / cols) + one)]
    
    for i in range(len(s_matrix)):
        for j in range(len(k_matrix[0])):
            for k in range(len(k_matrix)):
                r_matrix[i][j] += s_matrix[i][k] * k_matrix[k][j]
    return r_matrix

def get_dimensions(argv):
    lenght = len(argv[2])
    i = 0

    while (lenght > i*i):
        i += 1
    return i

def new_check_float(line, cols):
    i = 0

    if (len(line) % cols != 0):
        i = 1
    else:
        i = 0
    return i

def check_float(argv, cols):
    i = 0

    if (len(argv[1]) % cols != 0):
        i = 1
    else:
        i = 0
    return i