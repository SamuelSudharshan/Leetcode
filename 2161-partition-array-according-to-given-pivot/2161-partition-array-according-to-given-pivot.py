class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=0
        r=len(nums)-1
        rs=[0]*len(nums)
        for i,j in zip(range(len(nums)),range(len(nums)-1,-1,-1)):
            if nums[i]<pivot:
                rs[l]=nums[i]
                l+=1
            if nums[j]>pivot:
                rs[r]=nums[j]
                r-=1
        while l<=r:
            rs[l]=pivot
            l+=1
        return rs        