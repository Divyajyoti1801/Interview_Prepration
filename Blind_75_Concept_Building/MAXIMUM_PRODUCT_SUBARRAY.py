"""
Maximum Product Subarray

Given an integer array nums, find a 
subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


def maximum_product_subarray(nums=[]):
    curMax, curMin = 1, 1
    res = nums[0]

    for n in nums:
        vals = (n, n*curMax, n*curMin)
        curMax, curMin = max(vals), min(vals)

        res = max(res, curMax)

    return res


print("Maximum Product Subarray : ", maximum_product_subarray([2, 3, -2, 4]))
