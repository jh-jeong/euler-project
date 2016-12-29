'''
Created on 2015. 6. 23.

@author: biscuit
'''
# problem 36
# Double Palindromes

def is_Dpal(i):
    if not str(i) == str(i)[::-1]:
        return False
    b = bin(i)[2:]
    if not b == b[::-1]:
        return False
    return True

result = [i for i in range(1000000) if is_Dpal(i)]

print result
print sum(result)