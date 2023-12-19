class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        bk = [float('inf') for i in range(k)]
        pk = [0 for i in range(k)]

        for price in prices:
            bk[0] = min(bk[0], price)
            pk[0] = max(pk[0], price-bk[0])
            for i in range(1, k):
                bk[i] = min(bk[i], price-pk[i-1])
                pk[i] = max(pk[i], price-bk[i])
        return pk[-1]

        