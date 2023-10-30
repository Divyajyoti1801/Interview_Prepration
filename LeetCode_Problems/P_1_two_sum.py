"""
Problem Statement - 1 : Two Sum Problem

Problem Statement : 
    - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    - You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Time Complexity : O(n)
"""

def two_sum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement]!=i:
            return [i,hashmap[complement]]

print("Solution : Two Sum Problem: ")
print(two_sum([0,4,3,0],0))