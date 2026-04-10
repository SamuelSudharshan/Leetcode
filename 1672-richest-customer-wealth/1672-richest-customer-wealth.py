class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mw=0
        for i in accounts:
            mw = max(mw,sum(i))
        return mw