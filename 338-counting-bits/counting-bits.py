class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        mx = 1
        cur = 0

        for i in range(1, n+1):
            ans.append(ans[cur]+1)
            cur += 1

            if cur == mx:
                cur = 0
                mx <<= 1
        
        return ans