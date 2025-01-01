class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        d = 5

        while True:
            c = n // d
            d *= 5
            ans += c
            if c == 0:
                break
        
        return ans