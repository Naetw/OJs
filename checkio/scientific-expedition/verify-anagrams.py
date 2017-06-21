#!/usr/bin/env python3
# -*- coding: utf8 -*-

def verify_anagrams(first_word, second_word):
    first_word = ''.join(first_word.lower().split())
    second_word = ''.join(second_word.lower().split())

    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
