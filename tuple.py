# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:11:31 2026

@author: user
"""

t = (10,20,30,20,40)
print("tuple:",t)
print("first element:",t[0])
print("last element:",t[-1])
print("length:",len(t))
print("count of 20:",t.count(20))
print("index of 30:",t.index(30))
print("maximum:",max(t))
print("minimum:",min(t))
print("is 40 present:",40 in t)

l = list(t)
print("tuple converted to list:",l)

t2 = tuple(l)
print("list converted to tuple:",t2)
