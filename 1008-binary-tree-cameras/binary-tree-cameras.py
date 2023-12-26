# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def vc(root, i=False, c=True):
            if (root, i, c) in dp:
                return dp[(root, i, c)]

            if not root and not c:
                return float('inf')
            elif not root and c:
                return 0

            if i:
                a0 = vc(root.left, i=False, c=True) + vc(root.right, i=False, c=True)
                a1 = vc(root.left, i=True, c=True) + vc(root.right, i=True, c=True)
                dp[(root, i, c)] = min(a0, a1+1)
                return dp[(root, i, c)]
            if c:
                a00 = vc(root.left, i=False, c=False) 
                a01 = vc(root.left, i=False, c=True)
                a11 = vc(root.left, i=True, c=True) 
                
                b00 = vc(root.right, i=False, c=False) 
                b01 = vc(root.right, i=False, c=True)
                b11 = vc(root.right, i=True, c=True)

                a1 = a00 + b00
                a2 = a00 + b01
                a3 = a01 + b00
                a4 = a11 + b11

                ans = min(a1, a2, a3, a4+1)
                dp[(root, i, c)] = ans
                return ans

            if not i and not c:
                a1 = vc(root.left, i=True, c=True) + vc(root.right, i=True, c=True)
                dp[(root, i, c)] = a1+1
                return a1+1
        return vc(root)


            
            
            
            
            
            

            

        