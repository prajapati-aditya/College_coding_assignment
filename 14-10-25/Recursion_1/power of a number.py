    # using iteration
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
        
    half = power(base, exp//2)
    if exp % 2 == 0 :
        return half* half
    else :
        return base*half*half
        
    return power(base , rev)
