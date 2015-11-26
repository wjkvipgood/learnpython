#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):
    
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        if value < 800 or value > 2000:
            raise ValueError('width must between 800 ~ 2000!')
        self._width = value
        
    @property
    def height(self):
        return self._height
        
    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer')
        if value < 600 or value > 1500:
            raise ValueError('height must between 600 ~ 1500!')
        self._height = value
        
    @property
    def resolution(self):
        return self._height * self._width
        
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution