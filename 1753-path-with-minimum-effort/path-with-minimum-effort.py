class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        import heapq 
        heap = []

        m = len(heights)
        n = len(heights[0])
        dirn = [
            (1,0),  
            (-1,0),
            (0, 1),
            (0,-1)
        ]

        efforts = [[float("inf")] * n for _ in range(m)]

        # in heap we are pushing (effort so far , row , col  )
        heapq.heappush(heap, (0 , 0 , 0 ))

        while heap :
            effort , i , j = heapq.heappop(heap)
            print(i,j)
            if i == m-1 and j == n-1 : 
                print("here")
                return effort

            for x, y in dirn : 
                ni = i + x 
                nj = j + y 

                if 0 <= ni < m and 0 <= nj < n:
                    edge_cost = abs(heights[i][j] - heights[ni][nj])

                    new_effort = max(effort, edge_cost)
                    if new_effort < efforts[ni][nj]:
                        efforts[ni][nj] = new_effort
                        heapq.heappush(heap , (new_effort , ni , nj))

        
        return -1 

