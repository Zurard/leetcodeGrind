class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        path = 1
        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1 :
            return -1

        from collections import deque
        q = deque()
        q.append((0,0))

        visited = set()
        visited.add((0,0))
        dirn = [
                (-1, 0),   # Up
                (1, 0),    # Down
                (0, -1),   # Left
                (0, 1),    # Right
                (-1, 1),   # Top-right
                (-1, -1),  # Top-left
                (1, -1),   # Bottom-left
                (1, 1)     # Bottom-right
            ]


        def bfs():
            nonlocal path , n
            while q : 
                
                q_len = len(q)

                while q_len > 0 :
                    i,j = q.popleft()

                    if i == n-1 and j == n - 1 : 
                        return path
                    
                    # now we need to check all the 8 dirn for 0 and add it to the queue :
                    for x,y in dirn : 
                        ni = i + x 
                        nj = j + y 

                        if 0 <= ni < n and 0 <= nj < n :
                            if grid[ni][nj] == 0 and (ni, nj) not in visited:  
                                visited.add((ni,nj))
                                q.append((ni,nj))

                    q_len -= 1

                path+= 1
            return -1


        return bfs()