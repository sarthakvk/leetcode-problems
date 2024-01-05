from collections import deque

class RecentCounter:

    def __init__(self):
        self.arr = deque()
    
    def rm(self, val):
        while self.arr[0] < val-3000:
            self.arr.popleft()


    def ping(self, t: int) -> int:
        self.arr.append(t)
        self.rm(t)
        return len(self.arr)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)