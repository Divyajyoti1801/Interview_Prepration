"""
PARTITION TO K EQUAL SUM SUBSETS

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""


def partition_K_equal_sum_subsets(nums, k):
    total = sum(nums)
    if total % k:
        return False

    reqSum = total // k
    subSets = [0] * k
    nums.sort(reverse=True)

    def recursive(i):
        if i == len(nums):
            return True
        for j in range(k):
            if subSets[j] + nums[i] <= reqSum:
                subSets[j] += nums[i]

                if recursive(i+1):
                    return True
                subSets[j] -= nums[i]

                if subSets[j] == 0:
                    break
        return False
    return recursive(0)


print("Partition to K equal subsets sum : ",
      partition_K_equal_sum_subsets([4, 3, 2, 3, 5, 2, 1], 4))
