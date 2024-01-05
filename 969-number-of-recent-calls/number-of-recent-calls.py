class RecentCounter:

    def __init__(self):
        self.arr = []
    
    def lb(self, val):
        val -= 3000
        s = 0
        e = len(self.arr) - 1

        while s <= e:
            m = (s+e)//2

            if self.arr[m] < val:
                s = m + 1
            elif self.arr[m] > val:
                e = m - 1
            else:
                return m

        return e + 1
        

    def ping(self, t: int) -> int:
        self.arr.append(t)
        return len(self.arr) - self.lb(t)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)