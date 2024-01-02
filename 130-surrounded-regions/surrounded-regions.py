class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def bfs(x, y, nmap):
            if 0 > x or x >= m or y < 0 or y >= n:
                return
            if board[x][y] == 'X' or (x, y) in nmap:
                return
            nmap[(x, y)] = True
            
            bfs(x+1, y, nmap)
            bfs(x-1, y, nmap)
            bfs(x, y+1, nmap)
            bfs(x, y-1, nmap)

            if x == 0 or y == 0 or x + 1 == m or y+1 == n:
                nmap["block"] = True
            

        blocked = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    continue
                
                if not blocked.get((i,j)):
                    region = {}
                    bfs(i, j, region)
                    block = region.pop('block', False)

                    for x, y in region.keys():
                        if block:
                            if (x, y) in blocked:
                                break
                            blocked[(x, y)] = True
                        else:
                            board[x][y] = 'X'
                
            
            