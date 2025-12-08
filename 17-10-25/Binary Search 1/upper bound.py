arr = [2, 3, 7, 10, 11, 11, 25]
target = 3
res = len(arr)
low = 0 
high = len(arr)-1
while low < high :
    mid = (low+high) // 2
    if arr[mid] >= target :
        res = mid
        high = mid-1
        
    else :
        low = mid+1
print(res)