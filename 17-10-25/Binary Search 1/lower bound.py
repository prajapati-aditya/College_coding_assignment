arr = [2, 3, 7, 10, 11, 11, 25]
target = 111
# output = 3
low = 0
high = len(arr) - 1
res = len(arr)
while low <= high :
    mid = low + (high-low)  //2
    if arr[mid] >= target :
        res = mid
        high = mid-1
    
    else :
        low = mid+1
print(res)