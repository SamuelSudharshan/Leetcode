class Solution:
    def checkValidString(self, s: str) -> bool:
        l=0
        r=0
        for i in s:
            if i == '(':
                l+=1
                r+=1
            elif i == ')':
                r-=1
                l-=1
            else:
                l-=1
                r+=1
            if l<0:
                l=0
            if r<0:
                return False
        return l==0
            

        