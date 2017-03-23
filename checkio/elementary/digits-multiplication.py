#!/usr/bin/env python3
# -*- coding: utf8 -*-

def checkio(number):
    ans = 1
    for i in str(number).replace('0', ''):
        ans *= int(i, 10)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
