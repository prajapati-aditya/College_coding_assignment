if root is None :
            return res
        queue = deque()
        queue.append((root,0))
        curr_lvl = 0
        while queue :
            node,idx = queue.popleft()

            if idx == curr_lvl :
                res.append(node.val) 
                curr_lvl += 1
            if node.right:
                queue.append((node.right, idx+1))
            if node.left:
                queue.append((node.left, idx+1))
        return res
        