class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def findSteps(n):
            if n  == 1 :
                return 1 
            if n == 2 :
                return 2 
            
            if n in dp : 
                return dp[n]
            
            dp[n] = findSteps(n-1) + findSteps(n-2)   
            return dp[n]

        return findSteps(n)