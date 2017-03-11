#!/usr/bin/env python3
# -*- coding: utf8 -*-

'''
Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.

The list of banned words are as follows:

    sum
    import
    for
    while
    reduce
'''

def checkio(data):
    def s(numbers):
        if len(numbers) > 1:
            return numbers[-1] + s(numbers[:-1])
        else:
            return numbers[0]
    return s(data)

print (checkio([1,2,3]))
