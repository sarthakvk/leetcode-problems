class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        prnt = {}

        for i in range(n):
            lc = leftChild[i]
            rc = rightChild[i]

            if lc in prnt or rc in prnt:
                return False

            if lc >= 0:
                prnt[lc] = i
            
            if rc >= 0:
                prnt[rc] = i
        
        no_parent = 0
        root = None
        for i in range(n):
            if i not in prnt:
                root = i
                no_parent += 1
            if no_parent > 1:
                return False

        if no_parent != 1:
            return False
        
        tot = 0

        def dfs(root):
            nonlocal tot
            if root == -1:
                return
            tot += 1

            dfs(leftChild[root])
            dfs(rightChild[root])
        dfs(root)
        return tot == n