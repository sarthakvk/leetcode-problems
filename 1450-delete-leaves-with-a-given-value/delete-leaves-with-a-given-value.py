# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root, target):
            if not root:
                return True

            rml = dfs(root.left, target)
            rmr = dfs(root.right, target)

            if rml:
                root.left = None
            if rmr:
                root.right = None
            
            return rml and rmr and root.val == target
        
        if not dfs(root, target):
            return root