class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [-1] * len(nums)
        def helper(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            pick = nums[i] + helper(i+2)
            notpick = helper(i+1)
            dp[i]=max(pick,notpick)
            return dp[i]
        return helper(0)
