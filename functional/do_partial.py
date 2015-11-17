#!/usr/bin/env python3
# -*- coding: utf8 -*-

import functools

int2 = functools.partial(int, base = 2)

print('1000000 =', int2('100000'))
print('1010101 =', int2('1010101'))
