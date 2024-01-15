class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = {0:{},1:{}, 2:{}}

        for match in matches:
            winn = match[0]
            loser = match[1]

            if winn not in loss[2]:
                if winn not in loss[1]:
                    if winn not in loss[0]:
                        loss[0][winn] = True
            
            if loser in loss[0]:
                loss[1][loser] = True
                del loss[0][loser]
            elif loser in loss[1]:
                loss[2][loser] = True
                del loss[1][loser]
            elif loser not in loss[2]:
                loss[1][loser] = True
            

        zero_loss = list(loss[0].keys())
        one_loss = list(loss[1].keys())
        zero_loss.sort()
        one_loss.sort()

        ans = [zero_loss, one_loss]
        return ans
                    


        