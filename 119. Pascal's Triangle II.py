from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1]
        for i in range(0, rowIndex):
            nums[0] = nums[i] = 1
            nums_new = [1 for i in range(0, len(nums) + 1)]
            for j in range(1, len(nums)):
                nums_new[j] = nums[j] + nums[j-1]
            nums = nums_new
        return  nums
s = Solution()
nums = 3
p = s.getRow(nums)
print(p)