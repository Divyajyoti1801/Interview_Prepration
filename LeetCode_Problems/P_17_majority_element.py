"""
Problem - 17 : Majority Element 

Problem Statement: 
    - Given an array `nums` of size `n`, return the majority element*.
    - The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
"""

from collections import defaultdict


def majority_element(nums):
    n = len(nums)
    m  = defaultdict(int)
    for num in nums:
        m[num]+=1
    n = n//2
    for key,value in m.items():
        if value>n:
            return key
    return 0

print("Majority Element : ",majority_element([3,2,3]))