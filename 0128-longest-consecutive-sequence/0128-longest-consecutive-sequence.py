class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        l=0
        for t in n:
            if t-1 not in n:
                le=1

                while t + le in n:
                    le+=1
                l=max(l,le)
        return l


        