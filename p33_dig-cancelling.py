'''
Created on 2015. 6. 23.

@author: biscuit
'''
# problem 33
# Digit cancelling fractions

dc_frac = []

def verify_cancel(frac, digit):
    n, m = frac
    f_set = [[n*10+digit, m*10+digit],
             [n+digit*10, m*10+digit],
             [n*10+digit, m+digit*10],
             [n+digit*10, m+digit*10]]
    
    for i, j in f_set:
        if n*j == m*i:
            dc_frac.append((i,j))
    

frac_set = [(i, j) for i in range(1, 10) for j in range(1, 10) if i < j]

for k in range(1,10):
    for f in frac_set:
        verify_cancel(f, k)

print dc_frac
