"""
FREQUENCY OF THE MOST FREQUENT ELEMENT

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.


Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
"""


def frequency_of_the_most_frequent(nums, k):
    nums.sort()
    l, r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r-l+1) > total + k:
            total -= nums[l]
            l += 1
        res = max(res, r-l+1)
        r += 1
    return res


print("Frequency of the most frequent element: ",
      frequency_of_the_most_frequent([1, 2, 4], 5))
