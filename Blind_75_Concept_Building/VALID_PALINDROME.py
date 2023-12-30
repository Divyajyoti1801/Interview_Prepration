"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


def valid_palindrome(s=""):
    s = [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]


print("Valid Palindrome : ", valid_palindrome("A man, a plan, a canal: Panama"))
