"""
TWO SUMS

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""


def two_sums(nums=[], target=0):
    map = {}
    res = []

    for i, n in enumerate(nums):
        if map and (target-n in map):
            res.append(i)
            res.append(map[target-n])
            return res
        else:
            map[n] = i

    return res


print("Two Sums : ", two_sums([3, 2, 4], 6))
