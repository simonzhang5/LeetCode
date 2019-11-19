from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pn =1
        nums =0
        for i in range(len(digits)-1 , -1 , -1):
            nums = digits[i] * pn + nums
            pn = 10*pn
        nums += 1
        for i in range(len(digits)-1 , -1 , -1):
            digits[i] = nums % 10
            nums = nums // 10
        if nums > 0:
            digits.insert(0, 1)
        return digits
s = Solution()
nums = [9,9]
p = s.plusOne(nums)
print(p)

# time o(n) space o(n)