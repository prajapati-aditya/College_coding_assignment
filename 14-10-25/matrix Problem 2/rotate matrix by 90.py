matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
row = len(matrix)
col = len(matrix[0])
# find transpose
for r in range(row) :
    for c in range(r+1,col) :
        matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]
print(matrix)        
# reverse each row
for row in matrix :
    row.reverse()
print(matrix)
        
