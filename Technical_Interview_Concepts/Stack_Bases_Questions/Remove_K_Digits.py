"""
REMOVE K-DIGITS

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""


def remove_k_digits(nums, k):
    stack = []
    for c in nums:
        while k > 0 and stack and stack[-1] > c:
            stack.pop()
            k -= 1
        if stack or c != "0":
            stack.append(c)

    if k:
        stack = stack[:len(stack)-k]

    return "".join(stack) or "0"


print("Remove K Digits: ", remove_k_digits("1432219", 3))
