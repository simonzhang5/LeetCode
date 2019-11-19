from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if(rowIndex==0):
            return [1]
        dp = [1,1]
        for i in range(3, rowIndex+2):
            cur = [0]*(i)
            cur[0]=cur[-1]=1
            for j in range(1,i-1):
                cur[j] = dp[j-1]+dp[j]
            dp = cur
        return dp
s = Solution()
nums = 3
p = s.getRow(nums)
print(p)

#time O(k^2) space o(k)