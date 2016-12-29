'''
Created on 2015. 5. 12.

@author: biscuit
'''
# problem 23
# Non-abundant sums

import pyprimes as pp

def main():
    abundant = [n for n in range(1, 28124) if n < getDivSum(n)]
    nonAbSum = []
    
    sum = 0
    
    for i in range(1, 28124):
        for j in abundant:
            if (i < j):
                sum = sum + i
                break
            if (i - j in abundant):
                break
    
    print sum
                

def getDivSum(n):
    if n == 1:
        return 0
    sum = 1
    fact = pp.factorise(n)
    for p, e in fact:
        t = 0
        for i in range(e+1):
            t = t + p**i
        sum = sum * t
    return sum - n
        

if __name__ == '__main__':
    main()