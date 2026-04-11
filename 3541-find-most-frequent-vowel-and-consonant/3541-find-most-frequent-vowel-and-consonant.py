class Solution:
    def maxFreqSum(self, s: str) -> int:
        vmap={}
        cmap={}
        for i in s:
            if i in 'aeiou':
                vmap[i]=vmap.get(i,0)+1
            else:
                cmap[i]=cmap.get(i,0)+1
        m = max(vmap.values()) if vmap else 0
        mm = max(cmap.values()) if cmap else 0
        return m + mm        
            
        