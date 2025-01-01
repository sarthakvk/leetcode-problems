class Solution:
    def count_two_five(self, n):
        twos = 0
        fives = 0

        while n % 5 == 0:
            fives += 1
            n //= 5

        while n %2 == 0:
            twos += 1
            n //= 2
        
        return twos, fives

    def trailingZeroes(self, n: int) -> int:
        tt = 0
        tf = 0

        for i in range(2, n+1):
            t, f = self.count_two_five(i)
            tt += t
            tf += f
        
        return min(tt, tf)
        