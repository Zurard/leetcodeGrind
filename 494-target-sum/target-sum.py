class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def solve(index, value ):
            print(index , value)
            # dont know what to return in base condn  
            if index == len(nums):
                print(index, value)
                return 1 if value == target else 0

            if (index,value) in dp :
                return dp[(index,value)]

            pos = value +  solve(index+ 1 , value + nums[index])
            neg =value +  solve(index+ 1 , value - nums[index])
            dp[(index,value)] = pos + neg

            return dp[(index,value)]

        return solve(0,0)