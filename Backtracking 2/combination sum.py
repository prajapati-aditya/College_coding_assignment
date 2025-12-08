nums = [2,3,6,7]
target = 7
#Output: [[2,2,3],[7]]

sol = []
curr = []

def dfs(index,total=0) :
    # base case
    if total == target :
        sol.append(curr.copy())
        return 
    if total > target :
        return
    
    
    for i in range(index, len(nums)) :
        new_total = total + nums[i]
        curr.append(nums[i])
        # recurse
        dfs(i, new_total)
        curr.pop()
        
dfs(0)
print(sol)

        
        