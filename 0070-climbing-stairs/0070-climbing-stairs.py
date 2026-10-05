class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        res=0
        for i in range(3,n+1):
            res=a+b
            a=b
            b=res
        return n if n < 3 else res
         