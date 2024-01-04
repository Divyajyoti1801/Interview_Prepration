"""
BACKTRACKING CODING PATTERN : PERMUTATIONS

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permutations(nums=[]):
    res = []

    # Base-Case
    if (len(nums) == 1):
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)

        perms = permutations(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)

    return res


print("Permutations : ", permutations([1, 2, 3]))
