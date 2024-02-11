class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        tmp = temperatures
        n = len(temperatures)
        
        db = {}

        def warm_in(idx):

            val = tmp[idx]
            ans = float('inf')

            for i in range(val+1, 101):
                if i in db:
                    ans = min(ans, db[i]-idx)
            
            db[val] = idx
            
            if ans == float('inf'):
                ans = 0
            return ans

        for i in range(n-1, -1, -1):
            ans.append(warm_in(i))
        
        return ans[::-1]
        