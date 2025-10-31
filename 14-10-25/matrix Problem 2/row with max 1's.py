 
mat = [[0,0],[1,1],[0,0]]
index = -1
max_ones = -1
for ind , row in enumerate(mat) :
    print ( [ind, row] )
    ones_sum = sum(row)
    if ones_sum > max_ones :
        index = ind 
        max_ones = ones_sum 
print ([index,max_ones])
    
''' 
r = len(mat)
c = len(mat[0])
max_cnt = 0
rr  = 0 
for i in range(r) :
    count = 0
    for j in range(c) :
        if mat[i][j] == 1:
            count+=1
    if max_cnt < count :
        max_cnt = count
        rr = i 
print([rr,max_cnt]) 
'''
        
        
    