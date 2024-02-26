# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_h = 0
        self.sum = 0
    def driver(self, root, h=0):
        if not root:
            return
        
        if self.max_h == h:
            self.sum += root.val
        elif self.max_h < h:
            self.max_h = h
            self.sum = root.val
        
        self.driver(root.left, h+1)
        self.driver(root.right, h+1)
        

    def deepestLeavesSum(self, root: Optional[TreeNode], h=0) -> int:
        self.driver(root)
        return self.sum
        
        