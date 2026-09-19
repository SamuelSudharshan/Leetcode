class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if len(s)<len(t):
            return ""
        need={}
        for i in t:
            need[i]=need.get(i,0)+1
        w={}
        l=0
        start=0
        ml=float('inf')
        formed=0
        required=len(need)
        for r in range(len(s)):
            w[s[r]]=w.get(s[r],0) + 1
            if s[r] in need and w[s[r]] == need[s[r]]:
                formed+=1
                while formed == required:
                    g=r-l+1
                    if g<ml:
                        ml = g
                        start=l
                    w[s[l]]-=1
                    if s[l] in need and w[s[l]]<need[s[l]]:
                        formed-=1
                    l+=1
        if ml == float('inf'):
            return ""
        return s[start:start+ml]