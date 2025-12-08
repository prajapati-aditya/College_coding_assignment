adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
# output = [0, 2, 4, 3, 1]
stack = [0]
seen = set()
res = []
while stack :
    node = stack.pop()
    seen.add(node)
    res.append(node)
    
    for n in reversed(adj[node]) :
        if n not in seen :
            stack.append(n)
print(res)


'''v = len(adj)
seen = [False]*v
res = []

def dfs(node,seen,adj) :
    if seen[node] == True :
        return
    seen[node] = True
    res.append(node)
    
    for n in adj[node] :
        if seen[n] != True :
            dfs(n,seen,adj)
dfs(0,seen,adj)
print(res)'''