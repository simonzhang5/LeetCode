from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [0 for i in range(0,len(prices))]
        profit = 0
        for i in range(0, len(prices)-1):
            diff[i]= prices[i+1]- prices[i]
            profit = profit + max(0, diff[i])
        return profit
s = Solution()
nums = [7,1,5,3,6,4]
p = s.maxProfit(nums)
print(p)

#time o(n) space 0(n)