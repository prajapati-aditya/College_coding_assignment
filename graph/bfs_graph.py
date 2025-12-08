from collections import deque

adj= [[2, 3, 1], [0], [0, 4], [0], [2]]
# output = 0 2 3 1 4
q = deque()
q.append(0)
seen = set()
seen.add(0)
res = []

while q :
    node = q.popleft()
    res.append(node)
    for n in adj[node] :
        if n not in seen :
            seen.add(n)
            q.append(n)
print(res)