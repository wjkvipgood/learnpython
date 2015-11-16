#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(n):
    t = n
    m = 0
    while n>0:
        m = m*10 + n%10
        n = n//10
    return m == t 

output = filter(is_palindrome, range(1,1000))
print(list(output))
