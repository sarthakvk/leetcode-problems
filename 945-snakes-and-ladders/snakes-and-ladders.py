class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)

        def get_coordinate(num):
            nonlocal n
            row = n - 1 - (num - 1)//n

            if row % 2 == n % 2:
                if num % n == 0:
                    col = 0
                else:
                    col = (n - num%n)
            else:
                if num % n == 0:
                    col = n - 1
                else:
                    col = num%n - 1
            
            return row, col

        lvl = [[(1, False)]]
        visited = {}
        visited[(1, False)] = True
        def bfs():
            
            while lvl[-1]:
                nums = lvl[-1]
                q = []
                for num, jump in nums:
                    if num == n**2:
                        return len(lvl) - 1
                    x, y = get_coordinate(num)
                    for i in range(min(num+6, n**2), num, -1):
                        r, c = get_coordinate(i)
                        if board[r][c] != -1:
                            if (board[r][c], True) not in visited:
                                q.append((board[r][c], True))
                                visited[(board[r][c], True)] = True
                        elif (i, False) not in visited:
                            q.append((i, False))
                            visited[(i, False)] = True
                
                lvl.append(q)
            return -1
        return bfs()
