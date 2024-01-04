"""
BACKTRACKING CODE PATTERN : COMBINATION SUM

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""


def combination_sum(candidates=[], target=0):
    res = []

    def dfs(i, curr, total):
        # Base-Case
        if total == target:
            res.append(curr.copy())
            return

        if i >= len(candidates) or total > target:
            return

        # Including the candidate
        curr.append(candidates[i])
        dfs(i, curr, total+candidates[i])

        # Not Including the candidate
        curr.pop()
        dfs(i+1, curr, total)

    dfs(0, [], 0)
    return res


print("Combination Sum : ", combination_sum([2, 3, 6, 7], 7))
