matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
row = len(matrix)
col = len(matrix[0])

# Output: [[1,0,1],[0,0,0],[1,0,1]]
" checking initially if first row and first col is zero or not"
colFlag = False
rowFlag = False
for i in range(row) :
    if matrix[i][0] == 0  :
        colFlag = True 
for i in range(col) :
    if matrix[0][i] == 0 :
        rowFlag = True

# setting initials row and col to zero
for i in range(row) :
    for j in range(col) :
        if matrix[i][j] == 0 :
            matrix[i][0] = 0
            matrix[0][j] = 0
# print(matrix)

# now main changes
for i in range(1,row) :
    for j in range(1, col) :
        if matrix[i][0] == 0 or matrix[0][j] == 0 :
            matrix[i][j] = 0

" now we check and update first row and col"
if rowFlag == True :
    for i in range(col) :
        matrix[0][i] = 0
if colFlag == True :
    for i in range(row) :
        matrix[i][0] = 0

print(matrix)
