"""
MINIMUM SIZE SUBARRAY SUM

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""


def minimum_size_subarray(nums, target):
    l, total = 0, 0
    res = float("inf")

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r-l+1, res)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res


print("Minimum Size Subarray Sum : ",
      minimum_size_subarray([2, 3, 1, 2, 4, 3], 7))
