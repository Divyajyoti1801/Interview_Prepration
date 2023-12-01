"""
MINIMUM NUMBER OF FLIPS TO MAKE BINARY STRING ALTERNATING

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
"""


def minimum_number_of_flips(s):
    n = len(s)
    s = s + s  # major trick
    alt1, alt2 = "", ""

    for i in range(len(s)):
        alt1 += "0" if i % 2 else "1"
        alt2 += "1" if i % 2 else "0"

    res = len(s)
    diff1 = 0
    diff2 = 0
    l = 0  # left-pointer

    for r in range(len(s)):
        if s[r] != alt1[r]:
            diff1 += 1
        if s[r] != alt2[r]:
            diff2 += 1
        if (r-l+1) > n:
            if s[l] != alt1[l]:
                diff1 -= 1
            if s[l] != alt2[l]:
                diff2 -= 1
            l += 1

        if (r-l+1) == n:
            res = min(res, diff1, diff2)
    return res


print("Minimum number of flips to make Binary String Alternating: ",
      minimum_number_of_flips("111000"))
