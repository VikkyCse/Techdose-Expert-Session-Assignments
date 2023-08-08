#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0 
        for i in range(1,len(prices)):
            cost = prices[i]-mini
            profit = max(cost,profit)
            mini = min(prices[i],mini)
        return profit

