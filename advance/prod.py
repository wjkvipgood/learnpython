#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y, L)

print('prod([1,2,3,4]) =',prod([1,2,3,4]))
l = list(range(10))
l.pop(0)

print('prod([1,2,3,4,5,6,7,8,9,10]) =',prod(l))
