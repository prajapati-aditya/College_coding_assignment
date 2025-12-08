nums = [2,5,6,0,0,1,2]
target = 0
def search(nums,target) : 
    low =0
    high = len(nums)-1
    while low <= high :
        mid =(low+high) // 2
        if nums[mid] == target :
            return True 
        if nums[mid] == nums[low] and nums[mid] == nums[high] :
            low += 1
            high -= 1
        
        elif nums[mid] <= nums[low] :    # right side is sorted
            if target >= nums[mid] and target <= nums[high] :
                low = mid+1
            else :
                high = mid-1 
        else :
            if target >= nums[low] and target <= nums[mid] :
                high = mid-1
            else :
                low = mid+1
    return False
             
print(search(nums,target))