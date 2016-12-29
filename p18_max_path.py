'''
Created on 2015. 5. 11.

@author: biscuit
'''
# problem 18
# Maximum path sum I

def main():
    triangle = []
    maxSum = []
    path = raw_input("triangle data path: ")
    with open(path, "r") as f:
        for i, l in enumerate(f.readlines()):
            level = map(int, l.split())
            if not (len(level) == i+1):
                return -1
            triangle.append(level)
            maxSum.append([0]*(i+1))
    
    maxSum[-1] = triangle[-1]
    
    for i, l in list(enumerate(triangle))[-2::-1]:
        for j, v in enumerate(l):
            maxSum[i][j] = max(maxSum[i+1][j], maxSum[i+1][j+1]) + v
    
    print maxSum[0][0]
        
            

if __name__ == '__main__':
    main()

