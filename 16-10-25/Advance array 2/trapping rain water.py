nums = [4,2,0,3,2,5]
res = 0

for i in range (2,len(nums)-3) :
    if nums[i-1] > nums[i] or nums[i] < nums[i+1] :
        val = nums[i-1] - nums[i] - nums[i+1]
        res = res + abs(val)
    elif nums[i-1] == nums[i+1] :
        val = nums[i-1] - nums[i] 
        res += abs(val)
print(res)