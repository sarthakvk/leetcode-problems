# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def msum(root):
            if not root:
                return float('-inf'), float('-inf')
            
            s1, i1 = msum(root.left)
            s2, i2 = msum(root.right)

            ans = (
               max(s1, s2, 0) + root.val,
               max(i1, i2, s1+root.val, s2+root.val, s1+s2+root.val, root.val)
            )
            
            return ans
        
        return max(msum(root))

        