#!/usr/bin/env python3
# -*- coding: utf8 -*-

def construct_matrix(matrix, size, total):
    alter_flag = 1
    while total > 0:
        struct = list()
        for i in range(size):
            struct += [alter_flag]
            total -= alter_flag
            if total <= 0:
                struct[-1] += total
                struct += [0] * (size-i-1)
                break
            alter_flag = 1 if alter_flag != 1 else 2

        matrix.append(struct)
        if len(matrix[0])%2 == 0:
            alter_flag = 1 if alter_flag != 1 else 2
    

def decode_amsco(message, key):
    matrix = list()
    matrix.append([(idx, char) for idx, char in enumerate(str(key))])
    construct_matrix(matrix, len(matrix[0]), len(message))
    matrix = list(zip(*matrix))
    matrix = sorted(matrix, key=lambda x : x[0][1])
    base = 0
    chr_map = list()
    for idx, col in enumerate(matrix):
        chr_map.append([col[0]])
        for i in range(1, len(col)):
            chr_map[idx].append(message[base:base+col[i]])
            base += col[i]

    chr_map = list(zip(*sorted(chr_map, key=lambda x : x [0][0])))
    ans = ''.join(char for x in chr_map[1:] for char in x)
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
