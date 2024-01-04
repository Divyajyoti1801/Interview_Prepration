"""
BACKTRACKING CODING PATTERN : SUBSETS-II

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


def subsets_2(nums=[]):
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return

        # All subsets that include nums[i]
        subset.append(nums[i])
        backtrack(i+1, subset)
        subset.pop()

        # All subsets that don't include nums[i]
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(i+1, subset)

    backtrack(0, [])
    return res


print("Subsets - 2 : ", subsets_2([1, 2, 2]))
