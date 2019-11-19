from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         result = temp = nums[0]
#         for i in range(1, len(nums)):
#             if temp > 0:
#                temp += nums[i]
#                result = max(result, temp)
#             else:
#                 temp = nums[i]
#                 result = max(result, temp)
#         return result
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
s = Solution()
nums =[-2,1,-3,4,-1,2,1,-5,4]
p = s.maxSubArray(nums)
print(p)