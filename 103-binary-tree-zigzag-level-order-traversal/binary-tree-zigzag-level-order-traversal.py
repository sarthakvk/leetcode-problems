# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        flag = False
        ans = [[root]]
        h = 0

        while True:
            if not ans[h]:
                break
            
            if h + 1 == len(ans):
                ans.append([])

            nodes = ans[h]

            if flag:
                for i in range(len(nodes)-1, -1, -1):
                    n = nodes[i]
                    nodes[i] = n.val

                    if n.left:
                        ans[h+1].append(n.left)
                    if n.right:
                        ans[h+1].append(n.right)
            else:
                for i in range(len(nodes)-1, -1, -1):
                    n = nodes[i]
                    nodes[i] = n.val

                    if n.right:
                        ans[h+1].append(n.right)
                    if n.left:
                        ans[h+1].append(n.left)
            
            flag = not flag
            h += 1
        
        ans.pop(-1)

        return ans