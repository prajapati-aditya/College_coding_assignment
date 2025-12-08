v = 5
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
res = [[] for _ in range (v)]

print(res)

for (a,b) in edges :
    res[a].append(b)
    res[b].append(a)
print(res)