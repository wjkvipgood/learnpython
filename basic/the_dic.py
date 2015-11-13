#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'age': 25,
    'name': 'Jack',
    'Bob': 75,
    'd2':{
        'Michael': 95,
        'Bob': 75,
        'Tracy': 85
    }
}
print('d[\'age\'] =',d['age'])
print('d[\'name\'] =',d['name'])
print('d[\'d2\'][\'Michael\']',d['d2']['Michael'])
print('d.get(\'Thomas\', -1) =',d.get('Thomas', -1))
