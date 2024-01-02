"""
Find Minimum In Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""


def find_minimum_rotated_sorted_array(nums=[]):
    l = 0
    r = len(nums) - 1
    res = nums[0]

    while l < r:
        if (nums[l] < nums[r]):
            # Condition of Non-Rotated Array
            res = nums[l]
            break

        m = (l+r)//2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1  # Shifted to Right partition
        else:
            r = m - 1  # Shifted to Left Partition

    return res


print("Find minimum in rotated sorted array: ",
      find_minimum_rotated_sorted_array([3, 4, 5, 1, 2]))
