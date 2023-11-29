"""
LONGEST REPLACING CHARACTER REPLACEMENT

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

"""


def longest_repeating_character_replacement(s, k):
    count = {}
    res = 0
    l = 0
    maxF = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxF = max(maxF, count[s[r]])

        while (r-l+1) - maxF > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res


print("Longest repeating character replacement: ",
      longest_repeating_character_replacement("ABAB", 2))
