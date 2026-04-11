class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map={}
        c=0
        for i in nums:
            map[i]=map.get(i,0)+1
        for i in map:
            cn=map[i]*(map[i]-1)//2
            c+=cn
        return c

            
        