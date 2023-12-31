# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')

        def mindiff(root):
            nonlocal ans
            if not root:
                return

            lv = root.left
            rv = root.right

            while rv:
                if not rv.left:
                    rv = rv.val
                    break
                rv = rv.left
            if not rv:
                rv = float('inf')
            
            while lv:
                if not lv.right:
                    lv = lv.val
                    break
                lv = lv.right
            if not lv:
                lv = float('inf')
        
            ans = min(ans, abs(root.val-lv), abs(root.val-rv))

            mindiff(root.left)
            mindiff(root.right)
        
        mindiff(root)
        return ans
