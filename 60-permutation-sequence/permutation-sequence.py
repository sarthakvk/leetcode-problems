class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))

        fact = [0]*n
        num = k - 1
        i = 1
        while num > 0:
            fact[n-i] = num%i
            num //= i
            i += 1
        
        for i in range(n):
            val = fact[i]
            fact[i] = nums[val]
            nums.pop(val)
        
        return ''.join(map(str, fact))
