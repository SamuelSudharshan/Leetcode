class Solution:
    def maxProduct(self, n: int) -> int:
        ans=[]
        while n != 0:
            s=n%10
            ans.append(s)
            n//=10
        ans.sort()
        n=len(ans)
        return ans[n-1] * ans[n-2]
        