"""
GENERATE PARENTHESES

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""


def generate_parentheses(n):
    res = []
    stack = []

    def backtrack(open, close):
        if open == close == n:
            res.append("".join(stack))
            return

        if open < n:
            stack.append("(")
            backtrack(open+1, close)
            stack.pop()
        if close < open:
            stack.append(")")
            backtrack(open, close+1)
            stack.pop()

    backtrack(0, 0)
    return res


print("Generate Parentheses : ", generate_parentheses(4))
