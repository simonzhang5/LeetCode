from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = max_profit = 0
        for i in range(len(prices)-1):
            temp = max(0, prices[i+1]-prices[i]+temp)
            max_profit = max(max_profit, temp)
        return  max_profit
s = Solution()
nums = [7,1,5,3,6,4]
p = s.maxProfit(nums)
print(p)


# def maxProfit(self, prices: List[int]) -> int:
#     min_price = float('inf')
#     max_profit = 0
#     for i in range(len(prices)):
#         min_price = min(prices[i], min_price)
#         max_profit = max(max_profit, prices[i] - min_price)
#     return max_profit