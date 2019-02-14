# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 23:16:46 2019

@author: Matt Jure
"""

decimal = 0

hexadecimal = input("What's your hexadecimal today?")
for power, digit in enumerate(reversed(hexadecimal)):
    decimal+=int(digit, 16)*(16**power)
print(decimal)