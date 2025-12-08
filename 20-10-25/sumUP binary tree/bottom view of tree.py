'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        if not root : return []
        
        store = {}      # line : value
        q = deque()
        q.append((root,0))
        
        while q :
            node , line = q.popleft()
            
            if line not in store :
                store[line] = node.data
            else :  
                store[line] = node.data
            
            if node.left :
                q.append((node.left,line-1))
            if node.right :
                q.append((node.right, line+1))
        res = []
        for key in sorted(store) :
            res.append(store[key])
        return res