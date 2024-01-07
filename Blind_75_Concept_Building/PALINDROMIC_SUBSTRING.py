"""
Palindromic Substring

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

"""


def palindromic_substring(s=""):
    res = 0
    for i in range(len(s)):
        l = r = i
        res += count_palindrome(s, l, r)

        l = i
        r = i + 1
        res += count_palindrome(s, l, r)
    return res


def count_palindrome(s, l, r):
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    return res


print("Palindromic Substring : ", palindromic_substring("abc"))
