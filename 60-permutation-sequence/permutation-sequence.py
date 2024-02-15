class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = [None]*n
        cnt = 0
        def per(n, p=1):
            nonlocal cnt, k
            found = False
            if p > n:
                cnt += 1
                return cnt == k
            for i in range(1, n+1):
                if i in ans:
                    continue
                ans[p-1] = i
                found = per(n, p+1)

                if found:
                    break
                ans[p-1] = None

            return found
        
        per(n)
        return ''.join(map(str, ans))