class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        res=majority=0
        for i in nums:
            map[i]=1+map.get(i,0)
            if map[i] > majority:
                res=i
                majority=map[i]
        return res