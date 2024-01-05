"""
Combination Sum 2

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""


def combination_sum_2(candidates=[], target=0):
    res = []
    candidates.sort()

    def backtrack(pos, curr, target):
        if target == 0:
            res.append(curr[::])
            return
        if target <= 0:
            return

        prev = -1

        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            curr.append(candidates[i])
            backtrack(i+1, curr, target-candidates[i])
            curr.pop()

            prev = candidates[i]

    backtrack(0, [], target)
    return res


print("Combination Sum 2 : ", combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8))
