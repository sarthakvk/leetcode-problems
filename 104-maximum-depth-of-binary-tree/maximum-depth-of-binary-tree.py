# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def trav(root, dep=1):
            if not root:
                return 0

            return max(trav(root.left), trav(root.right)) + 1
        
        return trav(root)
