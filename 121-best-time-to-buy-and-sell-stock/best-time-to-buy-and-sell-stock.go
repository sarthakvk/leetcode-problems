func maxProfit(prices []int) int {
    profit := 0
    buy := prices[0]

    for _, i := range prices[1:] {
        if i < buy {
            buy = i
        }
        if i > buy {
            profit = max(profit, i-buy)
        }
    }
    return profit
}