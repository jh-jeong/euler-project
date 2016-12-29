'''
Created on 2015. 6. 23.

@author: biscuit
'''
# problem 34
# Digit factorial

from math import factorial

result = []

for i in range (3, 10000000):
    if sum(map(factorial, map(int, str(i)))) == i :
        result.append(i)

print result
