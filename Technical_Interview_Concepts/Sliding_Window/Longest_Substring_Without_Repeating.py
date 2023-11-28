"""
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def longest_substring_without_repeating_character(s):
    charSet = set()
    l = 0  # left-pointer
    res = 0  # result length

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res


print("Longest Substring Without Repeating Characters (abcabcbb) : ",
      longest_substring_without_repeating_character("abcabcbb"))
