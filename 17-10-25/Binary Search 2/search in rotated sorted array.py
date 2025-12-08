target = int(input("target: "))
nums = list(map(int,input("elements").split()))
'''  nums = [4,5,6,7,0,1,2], target = 0
    output = 4
'''

def search(nums,target) :
    low = 0
    high =len(nums)-1
    while low <= high :
        mid = (low+high) // 2
        
        if nums[mid] == target :
            return mid
        if nums[mid] >= nums[low] :     # left side is sorted
            if target >= nums[low] and target <= nums[mid] :
                high = mid-1
            else :
                low = mid+1
            
        else :    # right is sorted
            if target >= nums[mid] and target <= nums[high] :
                low = mid+1
            else :
                high = mid-1
                
    return -1    
print(search(nums,target))