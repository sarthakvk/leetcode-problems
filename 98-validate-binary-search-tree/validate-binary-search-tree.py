# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return True, float('inf'), -float('inf')
            
            if root.left and root.left.val >= root.val:
                return False, None, None
            if root.right and root.right.val <= root.val:
                return False, None, None
            
            l_valid, lmin, lmax = dfs(root.left)
            r_valid, rmin, rmax = dfs(root.right)

            if not l_valid or not r_valid:
                return False, None, None

            elif root.val <= lmax or root.val >= rmin:
                return False, None, None
            
            return True, min(root.val, lmin), max(rmax, root.val)
        
        ans, _, _= dfs(root)

        return ans


        