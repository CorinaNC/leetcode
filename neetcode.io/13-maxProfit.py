class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPurchase = prices[0]
        maxProfit = 0
        for price in prices:
            cur = price - minPurchase
            if cur > maxProfit:
                maxProfit = cur
            if price < minPurchase:
                minPurchase = price
        return maxProfit