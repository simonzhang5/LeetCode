from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
s = Solution()
numbers =[2,2,1,1,1,2,2]
p = s.majorityElement(numbers)
print(p)
# time o(n) space 0(n)