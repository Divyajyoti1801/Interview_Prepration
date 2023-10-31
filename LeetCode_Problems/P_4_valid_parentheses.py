"""
Problem - 4 : VALID PARENTHESIS

Problem Statement : 
    - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    - An input string is valid if:
        = Open brackets must be closed by the same type of brackets.
        = Open brackets must be closed in the correct order.
        = Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
"""

from inspect import stack


def valid_parenthesis(s):
    if len(s) == 0:
        return False
    stack = []
    dict = {"}":"{","]":"[",")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack==[] or dict[char]!=stack.pop():
                return False
        else:
            return False
    return stack == []
print("Valid Parentheses : ",valid_parenthesis("()"))
print()