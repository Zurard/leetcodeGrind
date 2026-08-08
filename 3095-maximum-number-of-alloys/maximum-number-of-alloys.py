class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """

        def safeHigh():
            return sum(stock) + budget 

        def canMake(x):
            for machine in range(k):
                total_cost = 0 
                for metal in range(n):
                    req = x * composition[machine][metal]

                    if req > stock[metal]: 
                        need = req - stock[metal]
                        total_cost += need * cost[metal]
                    
                    if total_cost > budget:
                        break
                
                if total_cost <= budget:
                    return True 
            
            return False

        
        low = 0 
        high = safeHigh()
            
        ans = 0     

        while low <= high : 
            x = (low+high) // 2

            if canMake(x):
                ans = x 
                low = x+1
            else :
                high = x - 1
    
        return ans