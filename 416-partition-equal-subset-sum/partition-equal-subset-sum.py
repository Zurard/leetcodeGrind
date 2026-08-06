from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        @cache
        def findSubset(index, current_sum):

            if current_sum == target:
                return True

            if current_sum > target:
                return False

            if index == len(nums):
                return False

            return (
                findSubset(index + 1, current_sum + nums[index]) or
                findSubset(index + 1, current_sum)
            )

        return findSubset(0, 0)
        # ------------  this is the standard way to solve this question ------------
        # dp = {} 
        # total = sum(nums)
        # if total % 2  == 1 :
        #     return False 
        
        # def findSubset(index , current_sum ):
            
        #     if current_sum == total // 2 :
        #         return True 
        #     if index == len(nums):
        #         return False 

        #     if current_sum > total // 2:
        #         return False
        #     if( index,current_sum) in dp :
        #         return dp[(index,current_sum)]

        #     take = findSubset(index + 1 , current_sum + nums[index])
        #     skip = findSubset(index+ 1 , current_sum)

        #     dp[(index, current_sum )] = take or skip 
        #     return dp[(index, current_sum )] 
        # return findSubset(0 , 0)























        # this soln cause TLE now need to find an another way to optimize it 
        # total = sum(nums)
        # dp = {}

        # def findSubsets(index, current_subset):

        #     subset_tuple = tuple(current_subset)

        #     if subset_tuple in dp:
        #         subset_sum = dp[subset_tuple]
        #     else:
        #         subset_sum = sum(current_subset)
        #         dp[subset_tuple] = subset_sum

        #     if total - subset_sum == subset_sum:
        #         return True

        #     if index == len(nums):
        #         return False

        #     current_subset.append(nums[index])
        #     if findSubsets(index + 1, current_subset):
        #         return True
        #     current_subset.pop()

        #     if findSubsets(index + 1, current_subset):
        #         return True

        #     return False

        # return findSubsets(0, [])