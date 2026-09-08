class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ml=0
        charset = set()
        left = 0
        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                ml =max(ml,right-left+1)
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left+=1
                charset.add(s[right])
        return ml
        

        