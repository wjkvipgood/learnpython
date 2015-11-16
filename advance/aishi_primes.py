#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#埃氏筛法计算素数
#

#1.构造一个从3开始的奇数序列（素数不可能是比2大的偶数）
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#2.定义一个不能被n整除的筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

#3.最后定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
