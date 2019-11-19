from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while (i < j):
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif (numbers[i]+numbers[j] < target):
                   i += 1
            else:
                   j -= 1
s = Solution()
numbers = [2,7,11,15]
target = 9
p = s.twoSum(numbers, target)
print(p)
# time o(n) space 0(n)

# from typing import List
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(numbers)-1
#         for m in range(0, len(numbers)):
#             if numbers[i]+numbers[j] > target:
#                 j -= 1
#             else:
#                if numbers[i]+numbers[j]<target:
#                    i += 1
#                else:
#                    break
#         return [i+1, j+1]