class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l < r:
            mid = (l+r)//2
            cw=0
            day=1
            for w in weights:
                if cw+w > mid:
                    day+=1
                    cw=w
                else:
                    cw+=w
            if day <= days:
                r=mid
            else:
                l = mid + 1
        return l
            