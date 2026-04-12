class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c,r=0,0
        for i in s:
            if i == "R":
                c+=1
            else:
                c-=1
            if c == 0:
                r+=1
        return r
        