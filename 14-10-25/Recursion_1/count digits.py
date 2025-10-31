def count(digit,num,div) :
    if num == 0 :
        return 0
    if digit !=0  and div % digit == 0 :
        return 1 + count(num%10 , num//10 , div)

div = 124
num =  div
print(count(num%10, num , div))









''' class Solution:
    
    def evenlyDivides( self,n):
        # code here
        count = 0
        div = n
        while n != 0 :
            digit = n % 10
            if digit != 0 :
                if div % digit == 0  :
                    count+=1
            n = n//10
        return count
res = Solution()
print(res.evenlyDivides(20)) '''
