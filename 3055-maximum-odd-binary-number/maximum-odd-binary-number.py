class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')

        ans = "1"*(ones-1)
        ans += "0"*(s.count('0'))
        ans += '1'

        return ans
        