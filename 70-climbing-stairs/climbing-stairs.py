class Solution:
    ans = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if n in self.ans:
            return self.ans[n]

        steps = self.climbStairs(n-1) + self.climbStairs(n-2)

        self.ans[n] = steps

        return steps
        
        