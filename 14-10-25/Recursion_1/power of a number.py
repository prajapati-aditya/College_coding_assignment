class Solution:
    def reverseexponentiation(self, n):
        
        # power calc using iteration
        def power(base , n ):
            res = 1 
            while n > 0 :
                if n % 2 == 1:
                    res = res * base
                
                base *= base
                n = n//2
            return res
        
        # power calc using recursion
        def pow_recr(base,exp) :
            if exp == 0 :
                return 1
            if n < 0 :
                return 1 / pow_recr(base, -exp) 
        
        base  = n
        # calculating reverse of the number
        rev = 0
        while n != 0 :
            rem = n % 10
            rev = rev*10 + rem
            n =  n // 10
        
        return power(base , rev)