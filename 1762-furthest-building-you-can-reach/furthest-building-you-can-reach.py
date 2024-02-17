from heapq import *

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bclimb = []

        if len(heights) < 2:
            return 0

        for b in range(len(heights)-1):
            if heights[b] >= heights[b+1]:
                continue
            
            b_need = heights[b+1] - heights[b]

            if b_need <= bricks:
                bricks -= b_need
                heappush(bclimb, -b_need)
            elif ladders > 0:
                if bclimb and -bclimb[0] > b_need:
                    bricks += (-heappop(bclimb) - b_need)
                    heappush(bclimb, -b_need)
                ladders -= 1
            else:
                return b
        
        return b + 1

