"""
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""


def container_with_most_water(heights=[]):
    max_water = float("-inf")

    l = 0
    r = len(heights) - 1

    while l < r:
        # Finding max-height
        recent_max_area = min(heights[l], heights[r]) * (r-l)
        max_water = max(max_water, recent_max_area)

        # Testing different heights
        if heights[l] >= heights[r]:
            r -= 1
        else:
            l += 1

    return max_water


print("Container with most water : ",
      container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
