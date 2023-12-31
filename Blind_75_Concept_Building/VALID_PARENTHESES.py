"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.


Input: s = "()"
Output: true
"""


def valid_parentheses(s=""):
    if len(s) == 0:
        return False

    check = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    stack = []

    for p in s:
        if p in check:
            stack.append(p)
        elif len(stack) == 0 or check[stack.pop()] != p:
            return False

    return len(stack) == 0


print("Valid Parentheses : ", valid_parentheses("()[]"))
