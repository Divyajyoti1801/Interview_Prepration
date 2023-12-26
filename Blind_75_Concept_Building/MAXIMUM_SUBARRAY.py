"""
Maximum Subarray

Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.


Algorithm : Kadane's Algorithm
    Initialize:
        max_so_far = INT_MIN
        max_ending_here = 0

    Loop for each element of the array

        (a) max_ending_here = max_ending_here + a[i]
        (b) if(max_so_far < max_ending_here)
                max_so_far = max_ending_here
        (c) if(max_ending_here < 0)
                max_ending_here = 0 
    return max_so_far
"""


def maximum_subarray(nums=[]):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print("The Maximum Subarray Sum : ", maximum_subarray(
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
