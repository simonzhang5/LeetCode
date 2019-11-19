from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts= collections.Counter(nums)
        return max(counts, key = counts.get)  #.keys()  .items()  .values()
#key关键字的作用是，对每个testlist元素先使用key指定的function来处理，然后再比较、返回预期的元素。
s = Solution()
numbers =[2,2,1,1,1,2,2]
p = s.majorityElement(numbers)
print(p)
# time o(n) space 0(n)

# dict = {}
# max_count = len(nums) // 2
# for i in range(0, len(nums)):
#     if (nums[i] not in dict):
#         dict[nums[i]] = 1
#     else:
#         dict[nums[i]] += 1
#         if (dict[nums[i]] > max_count):
#             return nums[i]
#      return nums[i]