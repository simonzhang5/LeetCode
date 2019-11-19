from typing import List
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        sums = 0
        for i in digits:
            sums = sums * 10 + i #10进制乘以10，进行累和；
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]
s = Solution()
nums = [1, 2, 3]
p = s.plusOne(nums)
print(p)

        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] != 9:
        #         digits[i] += 1
        #         return digits
        #     digits[i] = 0
        # digits[0] = 1
        # digits.append(0)
        # return digits
#time: o(n)  space:o(n) ->o(1)
