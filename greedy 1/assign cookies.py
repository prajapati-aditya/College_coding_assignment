g = [1,2,3]
s = [1,1]
#Output: 1
def solve(g,s) :
    n=len(g)
    m=len(s)
    g.sort()
    s.sort()
    l=0
    r=0
    while l<m and r<n :
        if g[r]<= s[l]:
            r+=1
        l+=1
    return r
print(solve(g,s))