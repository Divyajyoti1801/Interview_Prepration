"""
MAXIMUM SUBARRAY MIN-PRODUCTS

The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
"""


def maximum_subarray_min_products(nums):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)

    ans = 0
    stack = []

    for i, x in enumerate(nums + [float("-inf")]):
        while stack and stack[-1][1] >= x:
            _, xx = stack.pop()
            ii = stack[-1][0] if stack else -1
            ans = max(ans, xx * (prefix[i] - prefix[ii+1]))
        stack.append((i, x))

    return ans % 1_000_000_007


print("Maximum subarray min products : ",
      maximum_subarray_min_products([1, 2, 3, 2]))
