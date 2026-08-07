class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache
        @cache
        
        def solve (day, can_buy , transaction ) : 
            if day == len(prices) or transaction == 0 :
                return 0 
            
            if can_buy :
                buy = -prices[day] + solve(day+1, False , transaction)
                skip = solve(day+1, can_buy , transaction)
                return max(buy,skip)

            if not can_buy:
                sell = prices[day] + solve(day+1, True ,  transaction -1 )
                hold = solve(day+1, can_buy, transaction)
                return max (sell,hold)
            
        
        return solve(0,True,2)