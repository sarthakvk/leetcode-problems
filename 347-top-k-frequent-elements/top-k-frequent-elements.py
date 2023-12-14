from collections import Counter

class Val:
    def __init__(self, c, v):
        self.count = c
        self.val = v

class PQ:
    def __init__(self, cd):
        self.data = []

        for v, c in cd.items():
            vl = Val(c, v)
            self.data.append(vl)
        
        lp = (len(self.data) - 1) // 2

        for i in range(lp,-1,-1):
            self.hipifyDown(i)
    
    def get_root(self):
        if not self.data:
            return
        rt = self.data[0]

        le = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = le
            self.hipifyDown(0)

        return rt.val
    
    def hipifyUp(self, idx):
        if idx == 0:
            return

        prnt_idx = (idx-1) // 2

        if self.data[idx].count > self.data[prnt_idx].count:
            self.data[idx], self.data[prnt_idx] = self.data[prnt_idx], self.data[idx]
            self.hipifyUp(prnt_idx)
    
    def hipifyDown(self, idx):
        l = len(self.data)
        lc = 2*idx + 1
        rc = 2*idx + 2

        if lc >= l and rc >= l:
            return
        lcv = self.data[lc]
        rcv = None
        pv = self.data[idx]

        if rc < l:
            rcv = self.data[rc]
        
        if rcv is None:
            if lcv.count > pv.count:
                self.data[lc], self.data[idx] = self.data[idx], self.data[lc]
                self.hipifyDown(lc)
        else:
            if rcv.count > pv.count and rcv.count >= lcv.count:
                self.data[rc], self.data[idx] = self.data[idx], self.data[rc]
                self.hipifyDown(rc)
            elif lcv.count > pv.count and lcv.count >= rcv.count:
                self.data[lc], self.data[idx] = self.data[idx], self.data[lc]
                self.hipifyDown(lc)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()

        for i in nums:
            c[i] += 1
        
        pq = PQ(c)

        ans = []
        for i in range(k):
            rt = pq.get_root()
            ans.append(rt)
        
        return ans


        