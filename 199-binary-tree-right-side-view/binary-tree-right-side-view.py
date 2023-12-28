# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = {}
        queue = deque()

        queue.append((root, 0))

        while queue:
            node, height = queue.popleft()
            ans[height] = node.val
            
            if node.left:
                queue.append((node.left, height+1))
            if node.right:
                queue.append((node.right, height+1))
        out = []
        for i in range(len(ans.keys())):
            out.append(ans[i])
        
        return out


        