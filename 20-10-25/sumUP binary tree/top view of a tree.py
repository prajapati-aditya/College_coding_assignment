'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        # code here
        store = {}      # line : value
        q = deque()
        q.append((root,0))    # value : line
        
        if not root :
            return []
        
        while q : 
            node , line = q.popleft()
            
            if line not in store :
                store[line] = node.data
            
            if node.left :
                q.append((node.left,line-1))
                
            if node.right :
                q.append((node.right,line+1))
        
        res= []
        for key in sorted(store) :
            res.append(store[key])
        return res