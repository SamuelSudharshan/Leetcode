class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h=0
        for i, cit in enumerate(citations):
            if i + 1 <= cit:
                h=i+1
            else:
                break
        return h 
            