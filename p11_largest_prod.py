'''
Created on 2015. 5. 11.

@author: biscuit
'''
# problem 11
# Largest product in a grid

def main():
    M = input("grid height: ")
    N = input("grid width: ")
    
    grid = [None for _ in range(M)]
    max_prod = [[0 for _ in range(N)] for _ in range(M)]
    
    print "input the grid"
    
    for i in range(M):
        grid[i] = map(int, raw_input().split())
    
    for i in range(M):
        if i < 3:
            continue
        max_prod[i][0] = max(max_prod[i-1][0], 
                             grid[i][0] * grid[i-1][0] * grid[i-2][0] * grid[i-3][0])
        
    for j in range(N):
        if j < 3:
            continue
        max_prod[0][j] = max(max_prod[0][j-1], 
                             grid[0][j] * grid[0][j-1] * grid[0][j-2] * grid[0][j-3])    
        
    for i in range(1, M):
        for j in range(1, N):
            if i < 3 and j < 3:
                continue
            elif i < 3:
                max_prod[i][j] = max(max_prod[i-1][j],
                                     max_prod[i][j-1],
                                     grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3])
            elif j < 3:
                max_prod[i][j] = max(max_prod[i-1][j],
                                     max_prod[i][j-1],
                                     grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j])
            else:
                max_prod[i][j] = max(max_prod[i-1][j],
                                     max_prod[i][j-1],
                                     grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3],
                                     grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j],
                                     grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3],
                                     grid[i-3][j] * grid[i-2][j-1] * grid[i-1][j-2] * grid[i][j-3])
    
    print max_prod[M-1][N-1]
            
if __name__ == '__main__':
    main()


    
