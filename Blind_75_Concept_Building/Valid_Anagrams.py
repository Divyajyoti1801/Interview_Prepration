"""
VALID ANAGRAM

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""


def valid_anagram(s, t):
    return sorted(s) == sorted(t)


print("Valid Anagram : ", valid_anagram("anagram", "nagaram"))
