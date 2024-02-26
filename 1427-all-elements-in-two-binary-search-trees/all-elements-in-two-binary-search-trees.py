# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def pre(root):
            if root:
                yield from pre(root.left)
                yield root.val
                yield from pre(root.right)
        
        ans = []
        g1, g2 = pre(root1), pre(root2)
        
        try:
            v1 = next(g1)
        except:
            v1 = None
        
        try:
            v2 = next(g2)
        except:
            v2 = None


        while v1 is not None or v2 is not None:
            if v2 is None or (v1 is not None and v1 <= v2):
                ans.append(v1)
                try:
                    v1 = next(g1)
                except:
                    v1 = None
            elif v1 is None or (v2 is not None and v2 <= v1):
                ans.append(v2)
                try:
                    v2 = next(g2)
                except:
                    v2 = None
        
        return ans