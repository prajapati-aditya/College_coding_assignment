nums= [1,4,3,2]
def arrayPairSum(nums) -> int:
    nums.sort()
    summ = 0 
    for i in range(0,len(nums),2 ):
        summ += nums[i]
    return summ

print(arrayPairSum(nums))