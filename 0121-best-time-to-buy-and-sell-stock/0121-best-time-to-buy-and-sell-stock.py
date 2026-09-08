class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_buy = prices[0]
        max_profit = 0
        for num in prices:
            min_buy = min(min_buy,num)
            profit = num - min_buy
            max_profit = max(max_profit,profit)
        return max_profit