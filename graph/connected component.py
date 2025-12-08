n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

# Output: 2
" building adj list"
adj = [[] for _ in range(n)] 

for u,v in edges :
    adj[u].append(v)
    adj[v].append(u) 
    
# dfs function
def dfs(node) :
    
    for n in adj[node] :
        if not seen[n] :
            seen[n] = True
            dfs(n)
    
 
# for each edge do dfs 
seen = [False]*n
res = 0
for n in range(n) :
    if not seen[n] :
        seen[n] =True
        dfs(n)
        res += 1    
        
print(res)
        
