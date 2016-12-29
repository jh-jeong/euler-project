'''
Created on 2015. 5. 11.

@author: biscuit
'''
# problem 22
# Names scores


def main():
    path = raw_input("file path: ")
    names = []
    with open(path, "r") as f:
        buf = f.read()[1:-1]
        names = buf.split("\",\"")

    names.sort()
    
    result = 0
    for i, n in enumerate(names):
        result += (i+1) * getNameScore(n) 
        
    print result
        

def getNameScore(name):
    score = 0
    for c in name:
        score += ord(c)-64
    return score
        

if __name__ == '__main__':
    main()
