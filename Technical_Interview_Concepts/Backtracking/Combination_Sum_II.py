"""
COMBINATION SUM II

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""


def combination_sum_II(candidates, target):
    candidates.sort()

    res = []

    def backtrack(curr, pos, target):
        if target == 0:
            res.append(curr.copy())

        if target <= 0:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue

            curr.append(candidates[i])
            backtrack(curr, i+1, target-candidates[i])
            curr.pop()

            prev = candidates[i]

    backtrack([], 0, target)
    return res


print("Combination Sum II : ", combination_sum_II([10, 1, 2, 7, 6, 1, 5], 8))
