#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles():
    m = [1] 
    yield m
    while True:
        n = [1]
        t = list(range(len(m)-1))
        for i in t:
            n.append(m[i]+m[i+1])
        n.append(1)
        m = n
        yield n
