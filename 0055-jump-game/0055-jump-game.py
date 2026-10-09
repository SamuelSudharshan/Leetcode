class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        maxj=0
        for i in range(len(nums)):
            if i > maxj:
                return False
            maxj=max(maxj,i+nums[i])
            if maxj>=n-1:
                return True