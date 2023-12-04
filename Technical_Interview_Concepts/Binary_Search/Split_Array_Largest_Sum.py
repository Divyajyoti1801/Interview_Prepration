"""
SPLIT ARRAY LARGEST SUM

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
"""

# Binary-Search based solution


def split_array_largest_sum(nums, m):
    def check(guess):
        total = 0
        count = 1
        for i in nums:
            if total + i > guess:
                total = 0
                count += 1
            total += i
        return count > m
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = left + ((right-left)//2)
        if check(mid):
            left = mid + 1
        else:
            right = mid
    return left

# Dynamic Programming based solution


def split_array_largest_sum_DP(nums, m):
    dp = {}

    def dfs(i, m):
        if m == 1:
            return sum(nums[i:])
        if (i, m) in dp:
            return dp[(i, m)]

        res, curSum = float("inf"), 0
        for j in range(i, len(nums) - m + 1):
            curSum += nums[j]
            maxSum = max(curSum, dfs(j+1, m-1))
            res = min(res, maxSum)
            if curSum > res:
                break

        dp[(i, m)] = res
        return res
    return dfs(0, m)


print("Split Array Largest Sum : ",
      split_array_largest_sum([7, 2, 5, 10, 8], 2))
print("Split Array Largest Sum : ",
      split_array_largest_sum_DP([7, 2, 5, 10, 8], 2))
