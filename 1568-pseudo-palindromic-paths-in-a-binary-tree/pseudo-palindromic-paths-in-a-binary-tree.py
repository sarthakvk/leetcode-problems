# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        odd = Counter()
        even = Counter()

        def is_leaf(node):
            return (node.left is None and node.right is None)
        

        def dfs(root):
            nonlocal ans
            if not root:
                return
            in_even = False

            if root.val in odd:
                even[root.val] = odd[root.val]+1
                del odd[root.val]
                in_even = True
            elif root.val in even:
                odd[root.val] = even[root.val]+1
                del even[root.val]
            else:
                odd[root.val] += 1

            if is_leaf(root):
                if len(odd.keys()) == 1:
                    ans += 1
                elif len(odd.keys()) == 0 and len(even.keys()) > 0:
                    ans += 1
            else:
                dfs(root.left)
                dfs(root.right)

            if in_even:
                odd[root.val] = even[root.val]-1
                del even[root.val]
            else:
                even[root.val] = odd[root.val]-1
                del odd[root.val]
                if not even[root.val]:
                    del even[root.val]

        dfs(root)
        return ans


        