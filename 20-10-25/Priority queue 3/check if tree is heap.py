from collections import deque

class Solution:
    def isHeap(self, root):
        # code Here
        
        q = deque()
        q.append(root)
        foundNone = False
            
        while q :
            node = q.popleft()
            
            if not node : return True
                
            if node.left :
                if foundNone : return False
                    
                if node.left.data > node.data :
                    return False
                q.append(node.left)
                
            else :
                foundNone = True    
                        
            if node.right :
                if foundNone : return False
                    
                if node.right.data > node.data :
                    return False
                q.append(node.right)
                
            else :
                foundNone = True  
        return True
            