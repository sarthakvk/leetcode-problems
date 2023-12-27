# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def stree(p, i):
            if not p:
                return
            root = p[-1]
            idx = i.index(root)
            root = TreeNode(val=root)
            root.right = stree(p[idx:-1], i[idx+1:])
            root.left = stree(p[:idx], i[:idx+1])

            return root
        
        return stree(postorder, inorder)
