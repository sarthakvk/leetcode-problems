# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root, ans):
            if not root:
                ans.append(None)
                return

            inorder(root.left, ans)
            ans.append(root.val)
            inorder(root.right, ans)
            return ans

        def preorder(root, ans):
            if not root:
                ans.append(None)
                return
            
            ans.append(root.val)
            preorder(root.left, ans)
            preorder(root.right, ans)
        
        p1, p2, i1, i2 = [],[],[],[]

        inorder(p, i1)
        inorder(q, i2)
        preorder(p, p1)
        preorder(q, p2)

        if len(p1) != len(p2):
            return False
        
        for i, j, k, l in zip(p1, p2, i1, i2):
            if not ((i == j) and (k == l)):
                return False
        return True


        