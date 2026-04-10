class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        ls=[]
        for i in nums:
            sum+=i
            ls.append(sum)
        return ls
        