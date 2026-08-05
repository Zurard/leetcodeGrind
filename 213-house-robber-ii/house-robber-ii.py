class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp={}
        
        def maximize(n,nums):
            if n < 1:
                return 0

            if n == 1 :
                return nums[0] 
            
            if n in dp:
                return dp[n]

            dp[n] = max(maximize(n-1,nums), nums[n-1] + maximize(n-2,nums))
            return dp[n]

        nums1 = nums[1:] 
        nums2 = nums[:-1]
        
        ans1 = maximize(len(nums1) , nums1)
        dp.clear()
        ans2 = maximize(len(nums2) , nums2)
        return max(ans1, ans2)