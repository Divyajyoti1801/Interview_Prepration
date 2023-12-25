"""
132 PATTERN

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
"""


def pattern_132(nums):
    stack = []
    minLeft = nums[0]

    for n in nums:
        while stack and n >= stack[-1][0]:
            stack.pop()

        if stack and n < stack[-1][0] and n > stack[-1][1]:
            return False

        stack.append([n, minLeft])
        minLeft = min(n, minLeft)

    return False


print("132 Patters : ", pattern_132([1, 2, 3, 4]))
