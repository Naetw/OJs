#!/usr/bin/env python3
# -*- coding: utf8 -*-

def recall_password(cipher_grille, ciphered_password):
    ans = ''
    rotate = lambda x : [x[3][i] + x[2][i] + x[1][i] + x[0][i] for i in range(4)]
    for _ in range(4):
        for flag, char in zip(''.join(cipher_grille), ''.join(ciphered_password)):
            ans += char if flag == 'X' else ''
        cipher_grille = rotate(cipher_grille)
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
