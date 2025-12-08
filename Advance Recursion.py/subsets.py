nums = [1,2,3]
sol = []    # to store final result
curr = []   # to store current subsets

def solve(index) :
    # base case
    if index== len(nums) :
        sol.append(curr[:])
        return
    
    # pick
    curr.append(nums[index])
    solve(index+1)
    
    # not pick
    curr.pop()
    solve(index+1)

solve(0)
print(sol)