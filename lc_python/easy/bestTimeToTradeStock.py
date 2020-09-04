# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example 1:
#     Input: [7,1,5,3,6,4]
#     Output: 5
#     Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#     Input: [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transaction is done, i.e. max profit = 0.
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#---------This option takes too long - fails on 199/200
#         maxValue = 0
#         minValue = 0xFFFFFFFF
#         buyIndex = -1
#         sellIndex = -1
        
#         if len(prices) <= 1:
#             return 0
        
#         for i in range(0, len(prices)):
#             if prices[i] < minValue:
#                 minValue = prices[i]
#                 buyIndex = i
#                 for j in range(i + 1, len(prices)):
#                     if (prices[j] - prices[i] > maxValue):
#                         maxValue = prices[j] - prices[i]
#                         sellIndex = j
#         return maxValue
#

#---------This is also slow - track only min and max with 1 pass instead
#         maxValue = 0
#         minValue = 0xFFFFFFFF
#         buyIndex = -1
#         sellIndex = -1
#         buyPrice = 0xFFFFFFFF
#         sellPrice = 0
#         maxProfit = 0
        
#         if len(prices) <= 1:
#             return 0
        
#         for i in range(len(prices) - 1, -1, -1):
#             # print(prices[i])
#             if prices[i] > sellPrice:
#                 sellPrice = prices[i]
#                 buyPrice = 0xFFFFFFFF
#                 # print("sellPrice = %d" % sellPrice)
#                 for j in range(i - 1, -1, -1):
#                     if prices[j] < buyPrice:
#                         buyPrice = prices[j]
#                         # print("buyPrice = %d" % buyPrice)
#                         if sellPrice - buyPrice > maxProfit:
#                             maxProfit = sellPrice - buyPrice
#                             # print("maxProfit = %d - %d = %d" % (sellPrice, buyPrice, maxProfit))
#         return maxProfit
#---------This is much quicker and has only one pass
        maxValue = 0
        minValue = 0xFFFFFFFF
        maxProfit = 0
        
        for price in prices:
            if price > maxValue: # maxValue is found so find maxProfit
                maxValue = price
                if maxValue - minValue > maxProfit:
                    maxProfit = maxValue - minValue
            if price < minValue: # minValue is found so need new max
                minValue = price
                maxValue = 0
                
        return maxProfit
        
s = Solution()
listStocks = [7,1,5,3,6,4]
maxProfit = s.maxProfit(listStocks)
print("max profit = %d" % maxProfit)

