##
## EPITECH PROJECT, 2021
## 103cypher
## File description:
## 103cypher
##

import sys
import re
import math
from typing import Any
import re

def usage(argv):
    print("USAGE")
    print("    ./103cipher message key flag\n")
    print("DESCRIPTION")
    print("    message    a message, made of ASCII characters")
    print("    key    the encryption key, made of ASCII characters")
    print("    flag    0 for the message to be encrypted, 1 to be decrypted")

def error_handling(argv):

    if (str(argv[1]) == '-h'):
        usage(argv)
    if (len(argv) != 4):
        exit(84)
    

def sentence_to_ascii(argv):
    s_ascii = []

    for character in argv[1]:
        s_ascii.append(ord(character))
    return s_ascii


def key_to_ascii(argv):
    a = 1
    b = 0
    k_ascii = []

    for character in sys.argv[2]:
        k_ascii.append(ord(character))

    return k_ascii

def get_dimensions(argv):
    lenght = len(argv[2])
    i = 0

    while (lenght > i*i):
        i += 1
    return i

def empty_matrix(argv):
    i = get_dimensions(argv)
    rows, cols = (i, i)
    matrix = [[0 for i in range(cols)] for i in range(rows)]

    return matrix

##def key_matrix(argv):
##    len = get_dimensions(argv)
##    k_ascii = key_to_ascii(argv)
##
##    for number in k_ascii:
##

def check_float(argv, cols):
    i = 0

    if (len(argv[1]) % cols != 0):
        i = 1
    else:
        i = 0
    return i

def enc_prints(s_matrix, k_matrix, r_matrix):
    i = 0
    print("Key matrix:")
    ##while r_matrix(i) != None:
    ##    print(r_matrix[i])
    ##    i += 1
    j = 0
    counter = 0

    while i < len(k_matrix):
        j = 0
        while j < len(k_matrix[i]):
            if (j < len(k_matrix[i]) - 1):
                print(k_matrix[i][j], end ='\t')
                counter += 1
            else:
                print(k_matrix[i][j], end ='\n')
            j += 1
        i += 1
    
    if counter == 0:
        print("")
    print("")
    print("Encrypted message:")
    i = 0
    while i < len(r_matrix):
        j = 0
        while j < len(r_matrix[i]):
            if (i == len(r_matrix) - 1) and (j == len(r_matrix[i]) - 1):
                print(r_matrix[i][j], end ='\n')
            else:
                print(r_matrix[i][j], end =' ')                
            j += 1
        i += 1

def matrix_prod(s_matrix, k_matrix, cols, argv):
    one = check_float(argv, cols)

    r_matrix = [[0 for i in range(cols)] for i in range(math.trunc(len(argv[1]) / cols) + one)]
    for i in range(len(s_matrix)):
        for j in range(len(k_matrix[0])):
            for k in range(len(k_matrix)):
                r_matrix[i][j] += s_matrix[i][k] * k_matrix[k][j]
    return r_matrix

def encryption(argv):
    k = get_dimensions(argv)
    rows, cols = (k, k)
    result = check_float(argv, cols)
    k_matrix = [[0 for k in range(cols)] for k in range(rows)]
    s_matrix = [[0 for k in range(cols)] for k in range(math.trunc(len(argv[1]) / cols) + result)]
    key = key_to_ascii(argv)
    sentence = sentence_to_ascii(argv)
    matrix = empty_matrix(argv)
    i = 0
    j = 0
    a = 0

    while (j < rows):
        while (i < cols and a < len(key)):
            k_matrix[j][i] = key[a]
            a += 1
            i += 1
        i = 0
        j += 1

    a = 0
    i = 0
    j = 0

    while (j < len(argv[1])):
        while (i < cols and a <= len(sentence) - 1):
            s_matrix[j][i] = sentence[a]
            a += 1
            i += 1
        i = 0
        j += 1
    
    r_matrix = matrix_prod(s_matrix, k_matrix, cols, sys.argv)
    enc_prints(s_matrix, k_matrix, r_matrix)

#encryption(sys.argv)
def multiply_matrix(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    c = empty(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
                c[i][j] = total
    return (c)

def ascii_to_char(matrix):
    s = ''
    num = 0
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            num = matrix[i][j]
            if (num == 0):
                j += 1
            else:
                s = chr(num)
                print(s, end='')
                j += 1
        i += 1

def dec_prints(matrix, inverse_k):
    i = 0
    print("Key matrix:")
    j = 0
    counter = 0
    while i < len(inverse_k):
        j = 0
        while j < len(inverse_k[i]):
            if (j < len(inverse_k[i]) - 1):
                print(inverse_k[i][j], end ='\t')
                counter += 1
            else:
                print(inverse_k[i][j], end ='\n')
            j += 1
        i += 1
    print("Decrypted message:")
    ascii_to_char(matrix)

def decryption_e_matrix(argv, inverse_k):
    k = get_dimensions(argv)
    rows, cols = (k, k)
    line = [int(s) for s in re.findall(r'[-\d]+', argv[1])]
    result = new_check_float(line, cols)
    e_matrix = [[0 for k in range(cols)] for k in range(math.trunc(len(line) / cols) + result)]
    a = 0
    j = 0
    i = 0
    result = 0
    while (j < len(line)):
        while (i < cols and a <= len(line) - 1):
            e_matrix[j][i] = line[a]
            a += 1
            i += 1
        i = 0
        j += 1
    matrix = multiply_matrix(e_matrix, inverse_k)

    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            x = matrix[i][j]
            matrix[i][j] = round(x)
            j += 1
        i += 1
    dec_prints(matrix, inverse_k)

def decryption(argv):
    k = get_dimensions(argv)

    if (k == 1):
        rows, cols = (k, k)
        k_matrix = [[0 for k in range(cols)] for k in range(rows)]
        inverse_k = [0 for i in range(1)]
        key = key_to_ascii(argv)
        i, j, a = 0, 0, 0

        if (key == 0):
            return 84
        elif (k_matrix[0][0] > 0):
            while (j < rows):
                while (i < cols and a < len(key)):
                    k_matrix[j][i] = key[a]
                    a += 1
                    i += 1
                i = 0
                j += 1
            a = 0
            i = 0
            j += 1
        a = 0
        i = 0
        j = 0
        inverse_k[0] = 1/k_matrix[0][0]
        inverse_k[0] = float("{:.3f}".format(inverse_k[0]))

    if (k == 2):
        rows, cols = (k, k)
        k_matrix = [[0 for k in range(cols)] for k in range(rows)]
        inverse_k = [[0 for k in range(cols)] for k in range(rows)]
        key = key_to_ascii(argv)
        i, j, a = 0, 0, 0

        while (j < rows):
            while (i < cols and a < len(key)):
                k_matrix[j][i] = key[a]
                a += 1
                i += 1
            i = 0
            j += 1
        a = 0
        i = 0
        j = 0
        determinant = (k_matrix[0][0] * k_matrix[1][1]) - (k_matrix[0][1] * k_matrix[1][0])
        inverse_k[0][0] = k_matrix[1][1]
        inverse_k[0][1] = k_matrix[0][1] * -1
        inverse_k[1][0] = k_matrix[1][0] * -1
        inverse_k[1][1] = k_matrix[0][0]
        inverse_k[0][0] /= determinant
        inverse_k[0][1] /= determinant
        inverse_k[1][0] /= determinant
        inverse_k[1][1] /= determinant
        inverse_k[0][0] = float("{:.3f}".format(inverse_k[0][0]))
        inverse_k[0][1] = float("{:.3f}".format(inverse_k[0][1]))
        inverse_k[1][0] = float("{:.3f}".format(inverse_k[1][0]))
        inverse_k[1][1] = float("{:.3f}".format(inverse_k[1][1]))

    if (k == 3):
        rows, cols = (k, k)
        k_matrix = [[0 for k in range(cols)] for k in range(rows)]
        inverse_k = [[0 for k in range(cols)] for k in range(rows)]
        key = key_to_ascii(argv)
        i, j, a = 0, 0, 0
        error = "Matrix irreversible"

        while (j < rows):
            while (i < cols and a < len(key)):
                k_matrix[j][i] = key[a]
                a += 1
                i += 1
            i = 0
            j += 1
        a = 0
        i = 0
        j = 0
        determinant = (k_matrix[0][0] * k_matrix[1][1] * k_matrix[2][2]) + (k_matrix[0][1] * k_matrix[1][2] * k_matrix[2][0]) + (k_matrix[0][2] * k_matrix[1][0] * k_matrix[2][1]) - (k_matrix[2][0] * k_matrix[1][1] * k_matrix[0][2]) - (k_matrix[2][1] * k_matrix[1][2] * k_matrix[0][0]) - (k_matrix[2][2] * k_matrix[1][0] * k_matrix[0][1])
        inverse_k[0][0] = (k_matrix[1][1] * k_matrix[2][2]) - (k_matrix[1][2] * k_matrix[2][1])
        inverse_k[0][1] = ((k_matrix[0][1] * k_matrix[2][2]) - (k_matrix[0][2] * k_matrix[2][1])) * -1
        inverse_k[0][2] = (k_matrix[0][1] * k_matrix[1][2]) - (k_matrix[0][2] * k_matrix[1][1])
        inverse_k[1][0] = ((k_matrix[1][0] * k_matrix[2][2]) - (k_matrix[1][2] * k_matrix[2][0])) * -1
        inverse_k[1][1] = (k_matrix[0][0] * k_matrix[2][2]) - (k_matrix[0][2] * k_matrix[2][0])
        inverse_k[1][2] = ((k_matrix[0][0] * k_matrix[1][2]) - (k_matrix[0][2] * k_matrix[1][0])) * -1
        inverse_k[2][0] = (k_matrix[1][0] * k_matrix[2][1]) - (k_matrix[1][1] * k_matrix[2][0])
        inverse_k[2][1] = ((k_matrix[0][0] * k_matrix[2][1]) - (k_matrix[0][1] * k_matrix[2][0])) * -1
        inverse_k[2][2] = (k_matrix[0][0] * k_matrix[1][1]) - (k_matrix[0][1] * k_matrix[1][0])
        inverse_k[0][0] /= determinant
        inverse_k[0][1] /= determinant
        inverse_k[0][2] /= determinant
        inverse_k[1][0] /= determinant
        inverse_k[1][1] /= determinant  
        inverse_k[1][2] /= determinant
        inverse_k[2][0] /= determinant
        inverse_k[2][1] /= determinant
        inverse_k[2][2] /= determinant
        #inverse_k[0][0] = float("{:.3f}".format(inverse_k[0][0]))
        #inverse_k[0][1] = float("{:.3f}".format(inverse_k[0][1]))
        round(inverse_k[0][2])
        round(inverse_k[1][0]) 
        round(inverse_k[1][1])
        round(inverse_k[1][2])
        round(inverse_k[2][0])
        round(inverse_k[2][1])
        round(inverse_k[2][2])

    decryption_e_matrix(argv, inverse_k)

def loop(argv, a):
    num = []
    i = 0

    while argv[1][a] != ' ':
        num[i] = argv[1][a]
        print(num[i])
        print(argv[1][a])
        a += 1
        i += 1
    
    return num

def new_check_float(line, cols):
    i = 0

    #if (len(argv[1]) <= cols):
    #    return 0
    if (len(line) % cols != 0):
        i = 1
    else:
        i = 0
    return i

def matrix_product(s_matrix, k_matrix, cols, argv, line):
    one = check_float(argv, cols)

    r_matrix = [[0 for i in range(cols)] for i in range(math.trunc(len(line) / cols) + one)]
    
    for i in range(len(s_matrix)):
        for j in range(len(k_matrix[0])):
            for k in range(len(k_matrix)):
                r_matrix[i][j] += s_matrix[i][k] * k_matrix[k][j]
    return r_matrix

def empty(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(0)
    return (matrix)

def main(argv):
    error_handling(argv)
    if argv[3] == '0':
        encryption(argv)
    else:
        decryption(argv)

main(sys.argv)
