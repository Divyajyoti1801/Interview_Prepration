"""
Longest Palindromic Substring

Given a string s, return the longest 
palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

"""


def longest_palindromic_substring(s):
    res = ""
    resLen = 0

    for i in range(len(s)):
        # ODD-LENGTH : concept of expanding outwards
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l -= 1
            r += 1

        # EVEN-LENGTH
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return res


print("Longest Palindromic Substring : ",
      longest_palindromic_substring("babad"))
