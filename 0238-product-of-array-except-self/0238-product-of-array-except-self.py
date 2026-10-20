class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        out=[1]*n
        l=1
        for i in range(n):
            out[i]*=l
            l*=nums[i]
        r=1
        for i in range(n-1,-1,-1):
            out[i]*=r
            r*=nums[i]
        return out




