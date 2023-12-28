# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        def sums(root, sn=''):
            if not root:
                return
            elif not root.left and not root.right:
                nums.append(int(sn+str(root.val)))
            
            sn += str(root.val)
            sums(root.left, sn)
            sums(root.right, sn)
        
        sums(root)
        return sum(nums)

        