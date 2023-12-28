# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def cn(root, lh=None, rh=None):
            if not root:
                return 0
            
            if lh is None:
                lh = 0
                cur = root
                while cur:
                    lh += 1
                    cur = cur.left
            if rh is None:
                rh = 0
                cur = root
                while cur:
                    rh += 1
                    cur = cur.right
            
            if rh == lh:
                ans = 2**lh - 1
            else:
                ans = 1 + cn(root.left, lh=lh-1) + cn(root.right, rh=rh-1)

            return ans
        
        return cn(root)

        