class Solution:
    def reverseDegree(self, s: str) -> int:
        som=0
        for i in range(len(s)):
            c=123-ord(s[i])
            som+=c*(i+1)
        return som