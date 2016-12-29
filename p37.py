'''
Created on 2015. 6. 23.

@author: biscuit
'''
# problem 37
# Truncatable primes

import pyprimes as pp

def is_truncP(i):
    s = str(i)
    t = s[1:]
    while t != "":
        if not pp.isprime(int(t)):
            return False
        t = t[1:]
    
    t = s[:-1]
    while t != "":
        if not pp.isprime(int(t)):
            return False
        t = t[:-1]
    
    return True

result = []

p_iter = pp.primes_above(10)
cur = p_iter.next()

while len(result) != 11 :
    if is_truncP(cur):
        result.append(cur)
    cur = p_iter.next()
    
print result
print sum(result)