'''
Created on 2015. 6. 23.

@author: biscuit
'''
# problem 35
# Circular primes

import pyprimes as pp

pSet = []
result = []

with open("C:\prime_16000000.txt", "r") as f:
    s = f.read()
    pSet= map(int, s.split())[:78500]
    
    
def cPrime (i):
    temp = i
    s = str(i)[1:]+str(i)[0]
    i = int(s)
    while (i != temp):
        if not pp.isprime(i):
            return False
        s = s[1:]+s[0]
        i = int(s)
    return True

for i in pSet:
    if (i < 1000000) and (cPrime(i)):
        result.append(i)

print result
print len(result)
        