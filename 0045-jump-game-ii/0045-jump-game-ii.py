class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        far=0
        cure=0
        j=0
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i == cure:
                j+=1
                cure=far
        return j
