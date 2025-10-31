nums=[5,3,1,2]
# function to part the arry into two
def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr 

    mid = len(arr) //2 
    left = merge_sort(arr[:mid ])
    right = merge_sort(arr[mid:])
    
    return merge(left,right)
# function to merge both arrays
def merge(left,right) :
    res = [] 
    i = j = 0
    while i<len(left) and j<len(right) :
        if left[i] <= right[j] :
            res.append(left[i])
            i+=1
        else :
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
print(merge_sort(nums) )