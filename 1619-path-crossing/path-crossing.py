class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = {(0,0): True}
        curr = [0,0]
        for i in path:
            if i == "N":
                curr[1] += 1
            elif i == "S":
                curr[1] -= 1
            elif i == "W":
                curr[0] -= 1
            elif i == "E":
                curr[0] += 1
            
            n = (curr[0], curr[1])

            if n in points:
                return True
            points[n] = True
        
        return False
        