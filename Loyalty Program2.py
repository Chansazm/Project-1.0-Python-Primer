#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:29:27 2019

@author: chansa
"""
Customers = {'Chansa':200,'Chan': 700,'Nosiku': 7000,'Walter':11000}

points = range(0,10000)
for point in points:
    Platinum = point >= 5000;
    if not Platinum:
        Gold = point >= 1000;
        Silver = point >= 0;
        
