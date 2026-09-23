class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        while l < r:
            mid = (l + r)//2
            req_hour=0
            for pile in piles:
                req_hour += (pile+mid-1)//mid
            if req_hour > h:
                l = mid + 1
            else:
                r=mid
        return l
