class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        from functools import cache
        
        @cache
        def solve(day, can_buy, transaction_left):
            if day == len(prices) or transaction_left == 0: 
                return 0
            if can_buy : 
                buy = -prices[day] + solve(day+1, False , transaction_left)
                skip =  solve(day+1, can_buy, transaction_left)
                return max(buy , skip) 
            if not can_buy : 
                sell = prices[day] + solve(day+1, True , transaction_left - 1 )
                hold = solve(day+1, can_buy,  transaction_left)
                return max(sell , hold )
            
        return solve (0,True,1)
