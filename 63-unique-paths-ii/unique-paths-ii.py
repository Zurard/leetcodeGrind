class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp= {}
        m = len(grid)
        n = len(grid[0])

        def steps(i ,j ):
            if i < 0 or j < 0 : 
                return 0
            if i == 0 and j == 0 : 
                return 0 if grid[i][j] == 1 else 1
                # if grid[i][j] == 1 :
                #     return 0 
                # else:
                #     return 1
            if (i,j) in dp :
                return dp[(i,j)]

            # if its an obstacle 
            # print(i , j)
            if grid[i][j] == 1: 
                return 0 
             
            dp[(i,j)] = steps(i -1 ,j) + steps(i , j- 1)

            return dp[(i,j)]
        
        return steps(m- 1 , n -1  )