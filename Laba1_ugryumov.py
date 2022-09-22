# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:54:58 2022

@author: student
"""

import sys
from math import sqrt

a = float(input("Введите A: "))
if a == 0:
    print("A не может быть равно 0")
    sys.exit()
b = float(input("Введите B: "))
c = float(input("Введите C: "))
roots = []

if b == 0.0 and c == 0.0:
    roots.append(0)
elif b == 0.0 and c / a < 0.0:
    roots.append(sqrt(sqrt(-c / a)))
    roots.append(-sqrt(sqrt(-c / a)))
elif c == 0.0:
    roots.append(0.0)
    if b / a < 0.0:
        roots.append(sqrt(-b / a))
        roots.append(-sqrt(-b / a))
else:
    d = b ** 2 - 4.0 * a * c
    if d == 0.0 and b / 2.0 / a < 0.0:
        roots.append(sqrt(-b / 2.0 / a))
        roots.append(-sqrt(-b / 2.0 / a))
    elif d > 0.0:
        t1 = (-b + sqrt(d)) / 2.0 / a
        t2 = (-b - sqrt(d)) / 2.0 / a
        if t1 > 0.0:
            roots.append(sqrt(t1))
            roots.append(-sqrt(t1))
        if t2 > 0.0:
            roots.append(sqrt(t2))
            roots.append(-sqrt(t2))
            
cnt = 0
for i in roots:
    cnt += 1
print()
if cnt == 0:
    print('Нет корней.')
elif cnt == 1:
    print('1 корень:')
else:
    print(cnt, 'корня:')
for i in roots:
    print(i)