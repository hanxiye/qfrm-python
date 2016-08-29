# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
one = 0
two = 1
summ = 0
while (one+two) < 4000000:
    three = one + two
    one = two
    two = three
    if(two % 2 == 0):
        summ = two + summ
print summ

