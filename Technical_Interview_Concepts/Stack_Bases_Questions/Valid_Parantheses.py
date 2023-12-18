"""
VALID PARENTHESES

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

"""


def valid_parentheses(str):
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    if len(str) == 0:
        return False

    stack = []
    for s in str:
        if s in brackets.values():
            stack.append(s)
        elif s in brackets.keys():
            if (stack == []) or (brackets[s] != stack.pop()):
                return False
        else:
            return False
    return stack == []


print("Valid Parentheses : ", valid_parentheses("()"))
