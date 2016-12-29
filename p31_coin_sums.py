'''
Created on 2015. 5. 12.

@author: biscuit
'''
# problem 31
# Coin sums

val = [1, 2, 5, 10, 20, 50, 100, 200]

def getSols(sols, eqOrd, vec, sumVal):
    c_vec = vec[:]
    if eqOrd == 0:
        assert sumVal >= 0
        c_vec[0] = sumVal
        sols.append(c_vec)
        return
    pivot = sumVal / val[eqOrd]
    if pivot == 0:
        getSols(sols, eqOrd-1, c_vec, sumVal)
        return
    for i in range(0, pivot+1):
        c_vec[eqOrd] = i
        getSols(sols, eqOrd-1, c_vec, sumVal - i*val[eqOrd])

def main():
    res = []
    cur = [0, 0, 0, 0, 0, 0, 0, 0]
    getSols(res, 7, cur, 200)
    
    print len(res)
    
if __name__ == '__main__':
    main()
