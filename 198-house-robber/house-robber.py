class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def maximize(n) :
            if n < 1 :
                return 0 
            
            if n == 1 :
                return nums[0]
            
            if n in  dp : 
                return dp[n]

            dp[n] = max(maximize(n-1) , nums[n-1] + maximize(n-2))
            print(dp[n],n)
            return dp[n]

        return maximize(len(nums))