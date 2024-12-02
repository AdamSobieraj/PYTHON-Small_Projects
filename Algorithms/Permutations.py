# Given an array nums of distinct integers,
# return all the possible permutations.
# You can return the answer in any order
from typing import List

from numpy.random import permutation


# Imput: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2].....]

# Imput: nums = [0,1]
# Output: [[0,1],[1,0]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [] , []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans


# Usage example
solution = Solution()
nums = [1, 2, 3]
result = solution.permute(nums)

print(result)