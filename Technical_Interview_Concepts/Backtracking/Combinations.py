"""
COMBINATIONS

Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

You may return the answer in **any order**.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""


def combinations(n, k):
    res = []

    def backtrack(start, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return

        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
    backtrack(1, [])
    return res


print("Combinations : ", combinations(4, 2))
