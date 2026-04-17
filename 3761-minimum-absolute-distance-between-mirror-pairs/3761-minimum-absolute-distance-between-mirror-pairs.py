class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        map={}
        ans=float('inf')
        for i,n in enumerate(nums):
            if n in map:
                ans=min(ans,i-map[n])
            map[int(str(n)[::-1])]=i
        return -1 if ans==float('inf') else ans