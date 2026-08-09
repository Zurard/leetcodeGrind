class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        last_bad = -1
        last_min = -1
        last_max = -1 
        count = 0 

        for i in range(len(nums)):
            num =nums[i]            
            if num == minK :
                last_min = i 
            if num == maxK:
                last_max = i
            if num > maxK or num < minK:
                last_bad = i

            if last_min != -1 and last_max != -1 :
                boundary = min(last_min , last_max)
                if boundary >last_bad: 
                    count += boundary - last_bad

        return count 




        # this soln gives u TLE as this quesiion uses recursion without memoization 
        # count = 0

        # def findSubArrays(index, curr_arr):
        #     nonlocal count

        #     if index == len(nums):
        #         return

        #     curr_arr.append(nums[index])

        #     # If current element is outside the allowed range,
        #     # this subarray cannot be valid.
        #     if nums[index] < minK or nums[index] > maxK:
        #         curr_arr.pop()
        #         return

        #     if minK in curr_arr and maxK in curr_arr:
        #         count += 1

        #     findSubArrays(index + 1, curr_arr)

        #     curr_arr.pop()

        # for i in range(len(nums)):
        #     findSubArrays(i, [])

        # return count