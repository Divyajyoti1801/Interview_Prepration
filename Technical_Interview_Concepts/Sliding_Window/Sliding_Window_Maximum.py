"""
SLIDING WINDOW MAXIMUM

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
"""

from collections import deque


def sliding_window_maximum(nums, k):
    output = []
    q = deque()
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output


print("Sliding Window Maximum: ", sliding_window_maximum(
    [1, 3, -1, -3, 5, 3, 6, 7], 3))
