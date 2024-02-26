# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ssum = {}
        mod = 1e9 + 7
        ans = 0

        def dfs(root):
            if not root:
                return 0
            
            ssum[root] = dfs(root.left) + dfs(root.right) + root.val

            return ssum[root]
        
        def inorder(root, tsum):
            if not root:
                return
            nonlocal ans
            ss = ssum[root]
            ans = max(ans, (tsum-ss)*ss)

            inorder(root.left, tsum)
            inorder(root.right, tsum)
        
        dfs(root)
        inorder(root, ssum[root])
        # return ans
        return int(ans % mod)

            
