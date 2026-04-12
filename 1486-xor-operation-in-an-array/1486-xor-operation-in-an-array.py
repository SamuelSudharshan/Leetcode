class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ls=[]
        for i in range(n):
            ls.append(start+2*i)
        t=ls[0]
        for i in range(1,n):
            t^=ls[i]
        return t


