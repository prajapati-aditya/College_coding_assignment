arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3
def minPlatform(arr, dep):
    arr.sort()
    dep.sort()
        
    curr_plat = 0
    max_req = 0
    i = 0   # for arr
    j = 0   # for dep
        
    while i < len(arr) and j < len(dep) :
        if arr[i] <= dep[j] :
            curr_plat += 1
            max_req = max (max_req, curr_plat)
            i += 1
        else :
            curr_plat -= 1
            j += 1
                
    return max_req

print(minPlatform(arr,dep))       

        
    