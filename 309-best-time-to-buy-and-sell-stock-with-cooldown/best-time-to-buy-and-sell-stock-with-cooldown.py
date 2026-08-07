class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache 
        @cache 

        def solve(day,can_buy):
            if day >= len(prices):
                return 0 
            
            if can_buy : 
                buy = -prices[day] + solve(day+1 , False)
                skip = solve(day+1, True)
                return max(buy , skip)
            
            if not can_buy : 
                sell = prices[day] + solve(day+2 , True)
                hold = solve(day+1 , can_buy)
                return max(sell , hold )

        return solve(0,True)