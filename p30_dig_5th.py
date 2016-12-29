'''
Created on 2015. 5. 12.

@author: biscuit
'''
# problem 30
# Digit fifth powers

def main():
    res = []
    for i in range(360000):
        n = i
        p = 0
        while n != 0:
            p += (n % 10) ** 5
            n /= 10
        if i == p:
            res.append(i)
    
    res = res[2:]
    print sum(res)
              
if __name__ == '__main__':
    main()
