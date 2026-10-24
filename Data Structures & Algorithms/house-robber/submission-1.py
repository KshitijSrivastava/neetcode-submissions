class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}


        def robbing_calculator(nums, i, n):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = max(nums[i] + robbing_calculator(nums, i + 2, n), robbing_calculator(nums, i + 1, n))
            return dp[i]


        return robbing_calculator(nums, 0, len(nums))

        