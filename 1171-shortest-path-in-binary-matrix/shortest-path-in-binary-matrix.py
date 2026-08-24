class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        import heapq

        # (f, g, row, col)
        q = []

        def heuristic(i, j):
            return max(
                abs(i - (n - 1)),
                abs(j - (n - 1))
            )

        # g = actual cost from start
        g = 1

        # h = estimated cost to destination
        h = heuristic(0, 0)

        # f = g + h
        f = g + h

        heapq.heappush(q, (f, g, 0, 0))

        # Best actual cost found for every cell
        g_score = {}

        g_score[(0, 0)] = 1

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

        while q:

            f, g, i, j = heapq.heappop(q)

            # If this is an outdated heap entry, ignore it
            if g > g_score[(i, j)]:
                continue

            if i == n - 1 and j == n - 1:
                return g

            for x, y in dirn:

                ni = i + x
                nj = j + y

                if 0 <= ni < n and 0 <= nj < n:

                    if grid[ni][nj] != 0:
                        continue

                    ng = g + 1

                    # Only consider this path if it is better
                    if (ni, nj) not in g_score or ng < g_score[(ni, nj)]:

                        g_score[(ni, nj)] = ng

                        h = heuristic(ni, nj)
                        nf = ng + h

                        heapq.heappush(
                            q,
                            (nf, ng, ni, nj)
                        )

        return -1

        # this is the optimal soln to solve this 
        # path = 1
        # n = len(grid)

        # if grid[0][0] == 1 or grid[-1][-1] == 1 :
        #     return -1

        # from collections import deque
        # q = deque()
        # q.append((0,0))

        # visited = set()
        # visited.add((0,0))
        # dirn = [
        #         (-1, 0),   # Up
        #         (1, 0),    # Down
        #         (0, -1),   # Left
        #         (0, 1),    # Right
        #         (-1, 1),   # Top-right
        #         (-1, -1),  # Top-left
        #         (1, -1),   # Bottom-left
        #         (1, 1)     # Bottom-right
        #     ]


        # def bfs():
        #     nonlocal path , n
        #     while q : 
                
        #         q_len = len(q)

        #         while q_len > 0 :
        #             i,j = q.popleft()

        #             if i == n-1 and j == n - 1 : 
        #                 return path
                    
        #             # now we need to check all the 8 dirn for 0 and add it to the queue :
        #             for x,y in dirn : 
        #                 ni = i + x 
        #                 nj = j + y 

        #                 if 0 <= ni < n and 0 <= nj < n :
        #                     if grid[ni][nj] == 0 and (ni, nj) not in visited:  
        #                         visited.add((ni,nj))
        #                         q.append((ni,nj))

        #             q_len -= 1

        #         path+= 1
        #         return -1 


        # return bfs()