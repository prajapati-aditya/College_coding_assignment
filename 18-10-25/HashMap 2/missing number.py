class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_sum=0
        # finding sum of the range of elements that the array should have
        for i in range(len(nums)+1):
            full_sum+=i
        
        # find the sum of all elements in the array
        real_sum=0
        for num in nums:
            real_sum+=num
        
        return full_sum-real_sum