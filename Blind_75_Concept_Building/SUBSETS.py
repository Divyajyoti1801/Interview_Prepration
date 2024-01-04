"""
BACKTRACKING CODING PATTER : SUBSETS

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""


def subsets(nums=[]):
    res = []
    subset = []

    # Real Depth-First-Search
    def dfs(i):
        # Base-Case
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)

        # Decision to Not include nums[i]
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res


print("Subsets : ", subsets([1, 2, 3]))
