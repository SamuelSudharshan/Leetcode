class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[-1] * (n+1)
        def helper(n):
            if n < 3:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n]=helper(n-1)+helper(n-2)
            return dp[n]
        return helper(n)
         