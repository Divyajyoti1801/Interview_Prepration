"""
House Robber - 2

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""

from HOUSE_ROBBER import house_robber


def house_robber_2(nums=[]):
    return max(nums[0], house_robber(nums[1:]), house_robber(nums[:-1]))


print("House Robber - 2: ", house_robber_2([2, 3, 2]))
