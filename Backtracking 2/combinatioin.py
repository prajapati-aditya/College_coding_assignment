n = 4
k = 2

res = []
curr = []

def solve (index) :
    if len(curr) == k:
        res.append(curr.copy())
        return
    # termination
    if index > n :
        return
    
    for i in range(index, n+1) :
        curr.append(i)
        # recurse
        solve(i+1)
        #backtrack
        curr.pop()
solve(1)
print(res)