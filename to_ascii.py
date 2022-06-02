#!/usr/bin/env python3
import sys

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