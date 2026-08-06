class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0 
        dp={}
        
        def solve(x):
            if x < 0 :
                return float("inf")
            if x == 0 :
                return 0 
            if x in dp :
                return dp[x]
            best = float("inf")
            for coin in coins :
                best = min(best, 1 + solve(x - coin) )
            dp[x] = best
            return dp[x]
        
        ans = solve(amount)
        if ans == float("inf"):
            return -1 
        else :
            return ans 