class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])

        def findmin(i , j):
            if i < 0 or j < 0 :
                return float("inf")
            if i == 0 and j == 0 : 
                return grid[0][0]
            
            if (i,j) in dp :
                return dp[(i,j)]

            dp[(i,j)] = grid[i][j] + min(findmin(i-1, j) , findmin(i,j-1))
            return dp[(i,j)]

        return findmin(m - 1 , n -1)
            