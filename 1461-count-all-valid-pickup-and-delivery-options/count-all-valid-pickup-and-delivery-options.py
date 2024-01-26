class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        mod = 10**9+7

        for i in range(2*n, 1, -2):
            ans = (ans * ((i*(i-1))//2)%mod)%mod
        
        return ans