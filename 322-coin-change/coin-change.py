class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()

        # def bs(amount):
        #     s = 0
        #     e = len(coins) - 1


        #     while s <= e:
        #         m = (s+e)//2
        #         if coins[m] < amount:
        #             s = m + 1
        #         elif coins[m] > amount:
        #             e = m - 1
        #         else:
        #             return m
        #     return e
        sol = {}
        def dp(amount):
            if amount == 0:
                return 0

            if amount in sol:
                return sol[amount]

            ans = []

            for i in coins:
                if i <= amount:
                    t = dp(amount-i)
                    if t >= 0:
                        ans.append(t+1)

            if ans:
                a = min(ans)
            else:
                a = -1
            
            sol[amount] = a

            return a
        print(sol)
        return dp(amount)
            

