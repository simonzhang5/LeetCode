from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')#sys.maxsize
        max1 =0
        for i in range(0, len(prices)):
            if (prices[i] < mini ) :
                mini = prices[i]
            else:
                max1 = max(max1, int(prices[i]) - mini)
        return  max1
s = Solution()
nums = [7,1,5,3,6,4]
p = s.maxProfit(nums)
print(p)
#time o(n^2) space o(1)


# max1 = 0
# for i in range(0, len(prices) - 1):
#     for j in range(i + 1, len(prices)):
#         if (prices[j] > prices[i]) & (int(prices[j]) - int(prices[i]) > max1):
#             max1 = int(prices[j]) - int(prices[i])
# return max1
#time o(n^2) space o(1)