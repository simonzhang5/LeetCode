from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(numbers)):
            if (numbers[i] in dict):
                return [i+1, dict[numbers[i]]+1] if i< dict[numbers[i]] else [dict[numbers[i]]+1, i+1]
            else:
                dict[target -numbers[i]] = i
#        return False



        # dict = {}
        # for i in range(len(numbers)):
        #     dict[numbers[i]] = i
        # for j in range(len(numbers)):
        #     tmp = target - numbers[j]
        #     if (tmp in dict and dict[tmp] != j):
        #         return [j+1, dict[tmp]+1] if j< dict[tmp] else [dict[tmp]+1, j+1]
        #
        #
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         mapnum = [0 for i in range(0, max(numbers[-1]+1, target+1))]
#         mapindex = [0 for i in range(0, numbers[-1]+1)]
#         result = []
#         for i in range(0, len(numbers)):
#             mapnum[numbers[i]] = 1
#             mapindex[numbers[i]] = i+1
#         for j in range(0, len(mapnum)):
#             if mapnum[j] + mapnum[target -j] == 2:
#                 result = [mapindex[j], mapindex[target -j]]
#                 break
#         return result
s = Solution()
numbers = [2,7,11,15]
target = 9
p = s.twoSum(numbers, target)
print(p)
# time o(n) space 0(n)
