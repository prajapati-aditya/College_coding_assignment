grid = [[1,3,1],[1,5,1],[4,2,1]]
def path(grid,i,j) :
    if i < 0 or j < 0 :
        return float('inf')
    
    if i == 0 and j == 0 :
        return grid[i][j]
    x = path(grid,i-1,j)
    y = path(grid,i,j-1)
    return min(x,y) + grid[i][j]
print(path(grid,len(grid)-1 , len(grid[0])-1))