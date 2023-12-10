"""
PERMUTATIONS II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""


def permutations_II(nums):
    res = []
    prem = []
    count = {n: 0 for n in nums}
    for n in nums:
        count[n] += 1

    def dfs():
        if len(prem) == len(nums):
            res.append(prem[:])
            return

        for n in count:
            if count[n] > 0:
                prem.append(n)
                count[n] -= 1

                dfs()

                count[n] += 1
                prem.pop()
    dfs()
    return res


print("Permutations II : ", permutations_II([1, 1, 2]))
