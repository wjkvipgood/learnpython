#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(name):
    name = name.lower()
    name = name.capitalize()
    return name

L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))
