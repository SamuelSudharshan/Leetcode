class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        a=nums[l]
        b=nums[r]
        while b:
            a,b=b,a%b
        return a
            

        