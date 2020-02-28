#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 06:33:52 2020

@author: chansa
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n*factorial(n-1))
    


print(factorial(5))
    