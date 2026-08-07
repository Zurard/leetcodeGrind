class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_p = []

        for ch in p:
            if ch == "*" and new_p and new_p[-1] == "*":
                continue
            new_p.append(ch)

        p = "".join(new_p)
        from functools import cache 
        
        @cache 
        def solve(i,j):
            if j == len(p):
                return i == len(s)
            
            if i == len(s):
                while j  <  len(p):
                    if p[j] != "*":
                        return False 
                    j+=1
                return True 

            if s[i] == p[j] or p[j] == "?":
                return solve(i+1,j+1)
            
            if p[j] == "*" :
                return (solve(i,j+1) or solve(i+1 , j)) 
            
            return False
        
        return solve(0,0)