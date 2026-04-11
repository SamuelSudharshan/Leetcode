class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[0]*n
        lc,lcc,rc,rcc,=0,0,0,0
        for i in range(1,n):
            if boxes[i-1]=='1':lc+=1
            lcc+=lc
            ans[i]=lcc
        for i in range(n-2,-1,-1):
            if boxes[i+1] == '1':rc+=1
            rcc+=rc
            ans[i]+=rcc
        return ans
        