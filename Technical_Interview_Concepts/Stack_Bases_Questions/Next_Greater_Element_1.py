"""
NEXT GREATER ELEMENT - 1

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""


def next_greater_element_1(nums1, nums2):
    nums1Idx = {n: i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)

    for i in range(len(nums2)):
        if nums2[i] not in nums1Idx:
            continue
        for j in range(i+1, len(nums2)):
            if nums2[j] > nums2[i]:
                idx = nums1Idx[nums2[i]]
                res[idx] = nums2[j]
                break
    return res


def next_greater_element_2(nums1, nums2):
    res = [-1] * len(nums1)
    nums1Idx = {n: i for n, i in enumerate(nums1)}

    stack = []

    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and cur > stack[-1]:
            val = stack.pop()
            idx = nums1Idx[val]
            res[idx] = cur

        if cur in nums1Idx:
            stack.append(cur)

    return res


print("Next Greater Element: ",
      next_greater_element_1([4, 1, 2], [1, 3, 4, 2]))
