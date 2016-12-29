'''
Created on 2015. 5. 12.

@author: biscuit
'''
# problem 29
# Distinct powers

def main():
    rec = []
    for i in range(2, 101):
        for j in range(2, 101):
            rec.append(i**j)
            
    result = set(rec)
    print len(result)
              
if __name__ == '__main__':
    main()
