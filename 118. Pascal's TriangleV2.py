from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[[0]*n for n in range(1,numRows+1)] #n个数组
        for i in range(0,numRows):
            dp[i][0] = dp[i][-1] = 1
            for j in range(i+1):
                if(dp[i][j]==0):
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp
s = Solution()
nums = 5
p = s.generate(nums)
print(p)
#timeo(n^2)  space o(n^2)