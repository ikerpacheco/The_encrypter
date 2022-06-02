#!/usr/bin/env python3
from to_ascii import *

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

def enc_prints(s_matrix, k_matrix, r_matrix):
    i = 0
    print("Key matrix:")
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
    print("")
    print("Decrypted message:")
    ascii_to_char(matrix)
    print("")
