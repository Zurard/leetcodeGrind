class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import cache 

        @cache
        def solve(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0 

            if s[i] == t[j] : 
                take  = solve(i+1 , j+ 1)
                skip  = solve(i+1 , j)
                return take + skip
            
            return solve(i+1 , j)

        return solve(0,0)