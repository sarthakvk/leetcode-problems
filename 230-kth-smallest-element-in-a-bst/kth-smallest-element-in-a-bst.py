# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        terminate = False
        def inorder(root, idx=0):
            nonlocal k, ans, terminate
            if terminate:
                return -1000
            if not root:
                return 0
            
            li = inorder(root.left, idx=idx)

            idx = li + idx + 1
            if idx == k:
                ans = root.val
                terminate=True
    
            ri = inorder(root.right, idx=idx)
            return li + ri + 1
        
        inorder(root)
        return ans
            
