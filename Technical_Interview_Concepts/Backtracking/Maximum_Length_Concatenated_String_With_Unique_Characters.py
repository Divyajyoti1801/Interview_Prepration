"""
MAXIMUM LENGTH OF A CONCATENATED STRING WITH UNIQUE CHARACTERS

You are given an array of strings `arr`. A string `s` is formed by the **concatenation** of a **subsequence** of `arr` that has **unique characters**.

Return *the **maximum** possible length* of `s`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
"""

from collections import Counter


def maximum_length_concatenated_string_unique_character(arr):
    charSet = set()

    def overlap(charSet, s):
        c = Counter(charSet) + Counter(s)
        return max(c.values()) > 1

    def backTrack(i):
        if i == len(arr):
            return len(charSet)

        res = 0
        if not overlap(charSet, arr[i]):
            for c in arr[i]:
                charSet.add(c)
            res = backTrack(i+1)
            for c in arr[i]:
                charSet.remove(c)
        return max(res, backTrack(i+1))

    return backTrack(0)


print("Maximum Length concatenated string unique characters : ",
      maximum_length_concatenated_string_unique_character(["un", "iq", "ue"]))
