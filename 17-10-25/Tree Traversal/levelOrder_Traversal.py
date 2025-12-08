from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        q = deque()
        q.append(root)
        res=[]
        
        while q :
            lvl = []
            for _ in range(len(q)) :
                node = q.popleft()
                
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
                    
            res.append(lvl)
        return res