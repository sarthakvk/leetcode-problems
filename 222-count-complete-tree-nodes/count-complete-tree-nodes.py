# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        height = 0
        cur = root

        while cur.left:
            cur = cur.left
            height += 1
        
        ans = 2**height -1
        terminate = False

        def cl(root, h=1):
            nonlocal height, ans, terminate
            if not root:
                terminate = True

            if root and h > height:
                ans += 1
                return
            
            if not terminate:
                cl(root.left, h=h+1)
                cl(root.right, h=h+1)
        
        cl(root)
        return ans
        