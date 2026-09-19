class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f={}
        res=0
        i=0
        for j in range(len(s)):
            f[s[j]]=f.get(s[j],0)+1
            mf = max(f.values())
            cur = j-i+1
            if cur - mf > k:
                f[s[i]] -= 1
                i += 1
            res = max(res,j-i+1)
        return res