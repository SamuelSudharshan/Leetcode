class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        map={}
        sum=0
        for i,j in enumerate(s):
            map[j]=i
        for i,j in enumerate(t):
            sum+=abs(map[j]-i)
        return sum