class Node :
    def __init__(self,val):
        self.key = val
        self.left =None
        self.right = None 
        
class BST :
    def __init__(self,root):
        self.root = None 
        
    def insert(self, root , key) :
        if not root :       # we reached the end so create the node
            return Node(key) 
        if key < root.key :
            root.left = self.insert(root.left,key)      # the connection is made here only
        else :
            root.right =self.insert(root.right,key)
        return root 
    
    