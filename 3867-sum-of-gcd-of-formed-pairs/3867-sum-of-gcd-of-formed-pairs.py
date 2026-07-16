class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        prefixgcd=[]
        mx=0

        for num in nums:
            mx=max(mx,num)
            prefixgcd.append(gcd(num, mx))
        prefixgcd.sort()

        ans=0
        l=0
        r=len(prefixgcd)-1
        while l<r:
            ans+=gcd(prefixgcd[l],prefixgcd[r])
            l+=1
            r-=1
        return ans     