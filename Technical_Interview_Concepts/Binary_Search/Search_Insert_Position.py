"""
SEARCH INSERT POSITION

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""


def search_insert_position(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + ((r - l)//2)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return l


print("Search insert position : ", search_insert_position([1, 3, 5, 6], 5))
