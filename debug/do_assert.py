#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo(s):
    n = int(s)
    assert n != 0, 'n is ziro!'
    return 10 / n

def main():
    foo('0')

main()
