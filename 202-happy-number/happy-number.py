class Solution:
    def isHappy(self, n: int) -> bool:
        m = {}
        num = n

        while num not in m and num != 1:
            m[num] = True
            new = 0
            while num:
                new += (num % 10)**2
                num = num//10
            num = new
        
        if num == 1:
            return True
        return False
        