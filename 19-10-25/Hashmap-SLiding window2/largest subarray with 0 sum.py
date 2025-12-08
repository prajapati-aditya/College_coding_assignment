class Solution:
    def maxLength(self, arr):
        # code here
        maxLen = 0
        preSum = {0:-1}     # edge case, if sum becomes zero
        summ = 0
        
        for ind,num in enumerate(arr) :
            summ += num
            if summ not in preSum :
                preSum[summ] = ind
            else :
                length = ind - preSum[summ]
                maxLen = max(maxLen,length)
                
        return maxLen