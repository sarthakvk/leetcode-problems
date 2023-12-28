# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: (None, 1)}
        stack = [root]
        cur = root
        c = 2
        nodes = [p,q]
        while stack:
            node = stack.pop(-1)
            h = parent[node][1]
            if node.left:
                parent[node.left] = (node, h+1)
                stack.append(node.left)
            if node.right:
                parent[node.right] = (node, h+1)
                stack.append(node.right)
            
            if node.left in nodes or node.right in nodes:
                c -= 1
            
            if c == 0:
                break
        
        hp = parent[p][1]
        hq = parent[q][1]
        if hp > hq:
            while hp != hq:
                p = parent[p][0]
                hp -= 1
        elif hq > hp:
            while hq != hp:
                q = parent[q][0]
                hq -= 1

        while p is not q:
            p, _ = parent[p]
            q, _ = parent[q]
        
        return p