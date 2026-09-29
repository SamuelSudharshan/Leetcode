class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        fn=None
        c=0
        for num in nums:
            if c == 0:
                fn=num
            if num==fn:
                c+=1
            else:
                c-=1
        return fn

        