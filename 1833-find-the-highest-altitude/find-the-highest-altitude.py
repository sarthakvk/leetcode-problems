class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        ans = 0

        for n in gain:
            al = prev + n
            prev = al
            ans = max(ans, al)
        
        return ans