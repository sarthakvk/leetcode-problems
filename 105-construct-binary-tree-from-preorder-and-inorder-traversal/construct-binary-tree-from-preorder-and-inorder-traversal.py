# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        A = {}

        for i, j in enumerate(inorder):
            A[j] = i
        
        for i in range(1, len(preorder)):
            ptr = root
            val = preorder[i]
            while True:
                if A[val] < A[ptr.val]:
                    if ptr.left is None:
                        ptr.left = TreeNode(val=val)
                        break
                    ptr = ptr.left
                else:
                    if ptr.right is None:
                        ptr.right = TreeNode(val=val)
                        break
                    ptr = ptr.right
                
        return root