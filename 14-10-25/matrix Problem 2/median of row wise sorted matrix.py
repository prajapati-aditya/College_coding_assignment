import bisect
matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
# optimal solution --------------------- binary search
def bs (matrix) :
    row = len(matrix)
    col = len(matrix[0])
    median_index = (row*col+1)//2
    # find lowest and highest number
    low = min(row[0] for row in matrix) 
    high = max(row[-1] for row in matrix)
    # dow binary search 
    while low < high :
        mid = ( low+high )//2
        count = 0
        for row in matrix :
            count += bisect.bisect_right(row, mid)
        if count < median_index :
            low = mid+1
        else :
            high = mid
    return low
print (bs(matrix))

# Brute force approach --------------------------------

def brute(matrix) :

    arr = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m) :
        for j in range(n) :
            arr.append(matrix[i][j])
            
    print("matrix to array : ",arr)
    arr.sort()
    print("sorted array : ",arr )
    print("median = ", arr[len(arr)//2])

brute(matrix)