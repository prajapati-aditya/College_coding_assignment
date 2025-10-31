nums = [2,3,5,2,5,1,2]

def sum_arr(nums,idx) :
    if idx == len(nums) :
        return 0
    res = nums[idx] + sum_arr(nums,idx+1)
    return res

print(sum_arr(nums,0))