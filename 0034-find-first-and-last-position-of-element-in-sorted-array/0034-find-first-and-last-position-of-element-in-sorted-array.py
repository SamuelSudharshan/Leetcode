class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bs(nums, target, isl):

            left=0
            right=len(nums)-1
            idx=-1
            while left<=right:
                mid = (left + right)//2
                if nums[mid]>target:
                    right = mid - 1
                elif nums[mid]<target:
                    left = mid + 1
                else:
                    idx = mid
                    if isl:
                        right = mid - 1
                    else:
                        left = mid +1
            return idx
        r = bs(nums, target, True)
        l = bs(nums, target, False)
        return [r,l]
