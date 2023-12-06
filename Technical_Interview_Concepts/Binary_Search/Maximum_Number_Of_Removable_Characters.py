"""
MAXIMUM NUMBER OF REMOVABLE CHARACTERS


You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.

"""


def maximum_number_of_removable_character(s, p, removable):
    def isSubSeq(s, subSeq):
        i1, i2 = 0, 0

        while i1 < len(s) and i2 < len(subSeq):
            if i1 in removed or s[i1] != subSeq[i2]:
                i1 += 1
                continue
            i1 += 1
            i2 += 1
        return i2 == len(subSeq)

    res = 0
    l, r = 0, len(removable)-1
    while l <= r:
        m = l + ((r-l)//2)
        removed = set(removable[:m+1])

        if isSubSeq(s, p):
            res = max(res, m+1)
            l = m + 1
        else:
            r = m - 1

    return res


print("Maximum number of removable character: ",
      maximum_number_of_removable_character("abcacb", "ab", [3, 1, 0]))
