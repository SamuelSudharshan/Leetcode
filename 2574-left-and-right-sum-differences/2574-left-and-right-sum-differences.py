class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pref=0
        suff=sum(nums)
        ans=[]
        for i in nums:
            pref+=i
            ans.append(abs(pref-suff))
            suff-=i
        return ans


        