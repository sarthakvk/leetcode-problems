# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def sol(root):
            if not root:
                return 0, 0
            
            l1, ll = sol(root.left)
            r1, rr = sol(root.right)
            return max(l1, r1)+1, max(ll, rr, l1+r1)

        a1, a2 = sol(root)
        return max(a1-1, a2)

        