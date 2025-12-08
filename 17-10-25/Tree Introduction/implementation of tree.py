# taking input 
descriptions = []
row = int(input("enter rows: "))
for _ in range(row) :
    #a,b,c = map(int,input().split())
    #descriptions.append([a,b,c])
    
    descriptions.append(list(map(int,input().split())))
print(descriptions)
# ------------------------------------------------------
'''creating class'''
class Node :
    def __init__(self,val,left=None, right =None):
        self.val = val
        self.left = left 
        self.right = right

"making tree"
seen_nodes = {}      # storing nodes
has_parents = set()     # to store child with parent

for parent,child,lr in descriptions :
    if parent not in seen_nodes :
        seen_nodes[parent] = Node(parent)
        
    if child not in seen_nodes :
        seen_nodes[child] = Node(child)     
    
    if lr == 0 :    # left child
        seen_nodes[parent].left = seen_nodes[child]
        
    else :      # right child 
        seen_nodes[parent] = seen_nodes[child]
    
    has_parents.add(child)

"finding the root"
for parent,child,lr in descriptions :
    if parent not in has_parents :
        res = seen_nodes[parent]
print(res.val)    
    