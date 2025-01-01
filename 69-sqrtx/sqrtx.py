class Solution:
    def mySqrt(self, x: int) -> int:
        root = x
        if x == 0:
            return 0
        while True:
            ans = 0.5 * (root + (x/root))

            if abs(root - ans) < 1:
                break
            
            root = ans
        
        return int(ans)