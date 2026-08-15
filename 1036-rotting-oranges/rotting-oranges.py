class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        from collections import deque
        q = deque()
        
        n = len(grid)
        m = len(grid[0])

        fresh = 0 

        def findRotten():
            nonlocal m , n , fresh  
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2 :
                        q.append((i,j))
                    elif grid[i][j] == 1:
                        fresh += 1 


        time = 0 
        def bfs():
            nonlocal m , n , time , fresh 
            while q and fresh > 0:

                size = len(q)

                for _ in range(size):

                    i, j = q.popleft()

                    # Down
                    if i + 1 < n and grid[i + 1][j] == 1:
                        grid[i + 1][j] = 2
                        fresh -= 1
                        q.append((i + 1, j))

                    # Up
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        grid[i - 1][j] = 2
                        fresh -= 1
                        q.append((i - 1, j))

                    # Left
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        grid[i][j - 1] = 2
                        fresh -= 1
                        q.append((i, j - 1))

                    # Right
                    if j + 1 < m and grid[i][j + 1] == 1:
                        grid[i][j + 1] = 2
                        fresh -= 1
                        q.append((i, j + 1))

                time += 1
        
        findRotten()
        bfs()

        if fresh > 0 :
            return -1 
        
        return time 