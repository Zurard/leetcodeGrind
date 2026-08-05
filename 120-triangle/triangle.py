class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        m = len(triangle)
        n = len(triangle[0])

        if m == 1 and n == 1 :
            return triangle[0][0]

        def findmin( i , j ):
            print(i,j)
            if j > i :
                return float("inf") 
            if i == 0 and j == 0 :
                return triangle[0][0]
            if i < 0 or j < 0 : 
                return float("inf")
            if (i,j) in dp :
                return dp[(i,j)]
            
            dp[(i,j)] =triangle[i][j] +  min(findmin(i-1,j) , findmin(i-1,j-1))
            return dp[(i,j)] 
        
        answer = min(findmin(m-1, j) for j in range(len(triangle[-1])))
        return answer