class Solution:
    def minInsertions(self, s: str) -> int:
        from functools import cache
        
        @cache
        def findLongest(l,r):
            if l > r :
                return 0 
            if l == r :
                return 1 

            if s[l] == s[r]:
                return 2 + findLongest(l+ 1 , r -1)

            if s[l] != s[r]: 
                return max(findLongest(l+ 1 , r),findLongest(l, r -1)) 

        return len(s) - findLongest(0, len(s) - 1)