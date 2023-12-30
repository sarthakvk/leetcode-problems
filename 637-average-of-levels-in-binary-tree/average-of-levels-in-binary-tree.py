# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        def dfs(root, h=0):
            if not root:
                return
            
            if h == len(ans):
                ans.append((root.val, 1))
            else:
                ans[h] = (ans[h][0] + root.val, ans[h][1]+1)

            dfs(root.left, h=h+1)
            dfs(root.right, h=h+1)
        
        dfs(root)

        return [i/j for i, j in ans]


        