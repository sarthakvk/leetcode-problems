# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        rc = root.right
        lc = root.left
        root.left = None
        
        if rc and lc:
            root.right = lc
            while lc.right:
                lc = lc.right
            lc.right = rc
        elif lc:
            root.right = lc
    
        return root