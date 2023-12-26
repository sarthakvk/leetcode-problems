# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        m = {}
        def bfs(root, lvl=0):
            if not root:
                l = m.setdefault(lvl, [])
                l.append(root)
                return
            
            l = m.setdefault(lvl, [])
            l.append(root.val)
            bfs(root.left, lvl=lvl+1)
            bfs(root.right, lvl=lvl+1)
        
        bfs(root)
        for k, v in m.items():
            i, j = 0, len(v)-1

            while i < j:
                if v[i] != v[j]:
                    return False
                i += 1
                j -= 1
        return True

            
            

        