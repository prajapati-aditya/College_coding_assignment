nums = [1,2,3]
res = []
curr = []
seen = set()

def solve() :
    # base case
    if len(curr) == len(nums) :
        res.append(curr.copy())
        return
    
    for num in nums :
        if num not in seen :
            seen.add(num)
            curr.append(num)
            
            solve()
            curr.pop()
            seen.remove(num)
            
solve()
print(res)          