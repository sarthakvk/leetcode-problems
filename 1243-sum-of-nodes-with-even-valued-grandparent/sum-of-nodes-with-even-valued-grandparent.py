# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        parent = {}
        ans = []

        def get_gp(node):
            if node in parent:
                p = parent[node]
                if p in parent:
                    return parent[p]

        def dfs(root):
            if not root:
                return
            gp = get_gp(root)
            if gp and gp.val % 2 == 0:
                ans.append(root.val)

            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)
        dfs(root)
        return sum(ans)