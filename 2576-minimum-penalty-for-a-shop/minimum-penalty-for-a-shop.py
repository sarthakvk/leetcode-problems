class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = float('inf')
        out = None
        a = 0
        b = 0
        for i in customers:
            if i == 'Y':
                a += 1
        
        for i in range(len(customers)):
            if ans > b+a:
                out = i
            ans = min(ans, b+a)

            if customers[i] == 'Y':
                a -= 1
            else:
                b += 1
        
        if ans > b+a:
            out = i+1
        return out