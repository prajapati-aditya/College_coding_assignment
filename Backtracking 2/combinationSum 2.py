candidates = [10,1,2,7,6,1,5]
target = 8
'''Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
] '''

candidates.sort()
n = len(candidates)
res = []
curr = []

def solve(index,remains) :
    if remains == 0 :
        res.append(curr.copy())
        return
    if index >= n :
        return
    if candidates[index] > remains :
        return
    
    for i in range(index,n) :
        if i >index and candidates[i] == candidates[i-1] :
            continue
        num = candidates[i]
        curr.append(num)
        
        solve(i+1, remains-num)
        
        curr.pop()
        
solve(0,target)
print(res)