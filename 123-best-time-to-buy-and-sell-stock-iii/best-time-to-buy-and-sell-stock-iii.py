class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0

    buy1, buy2 = float('inf'), float('inf')
    p1, p2 = 0, 0

    for price in prices:
        buy1 = min(buy1, price)
        p1 = max(p1, price - buy1)

        buy2 = min(buy2, price - p1)
        p2 = max(p2, price - buy2)

    return p2