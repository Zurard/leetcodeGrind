class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_diff = -1
        l = 0 
        r = 1

        while r < len(nums) and l <= r: 
            if r > l and nums[l] < nums[r]  : 
                diff = nums[r] - nums[l]
                if max_diff < diff:
                    max_diff = diff
                r+=1
                continue 
            elif l == r  :
                r +=1 
            else : 
                l+=1

        return max_diff 