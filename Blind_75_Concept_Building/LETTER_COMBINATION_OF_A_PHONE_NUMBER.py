"""
Letter Combination Of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


def letter_combination_phone_number(digits=""):
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(i, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return

        for c in digitToChar[digits[i]]:
            backtrack(i+1, curr + c)

    if digits:
        backtrack(0, "")

    return res


print("Letter Combination of a phone number : ",
      letter_combination_phone_number("23"))
