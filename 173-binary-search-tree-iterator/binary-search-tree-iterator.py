# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = [-1]
        self.index = 0
        self.create(root)
    
    def create(self, root):
        if not root:
            return

        self.create(root.left)
        self.inorder.append(root.val)
        self.create(root.right)

    def next(self) -> int:
        if self.index + 1 < len(self.inorder):
            self.index += 1
            return self.inorder[self.index]
        return -1

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.inorder)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()