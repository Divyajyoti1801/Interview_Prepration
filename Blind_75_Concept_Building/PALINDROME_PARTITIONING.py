"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""


def palindrome_partitioning(s=""):
    res = []
    part = []

    def dfs(i):
        if i >= len(s):
            res.append(part[::])
            return

        for j in range(i, len(s)):
            if isPalindrome(s, i, j):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()

    dfs(0)
    return res


def isPalindrome(s="", l=0, r=0):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
    return True


print("Palindrome Partitioning : ", palindrome_partitioning("aab"))
