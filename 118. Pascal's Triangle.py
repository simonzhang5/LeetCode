from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [1]
        result = []
        for i in range(0, numRows):
            nums[0] =nums[i] = 1
            nums_new = [0 for i in range(0, len(nums) + 1)]
            for j in range(1,len(nums)):
                nums_new[j] = nums[j] + nums[j-1]
            reuslt = result.append(nums)
            nums = nums_new
        return result
s = Solution()
nums = 5
p = s.generate(nums)
print(p)