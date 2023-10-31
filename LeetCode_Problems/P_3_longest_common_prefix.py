"""
Problem - 3 : LONGEST COMMON PREFIX

Problem Statement : 
    - Write a function to find the longest common prefix string amongst an array of strings.
    - If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

def longest_common_prefix(str):
    # Base-Case
    res = ""
    
    for i in range(len(str[0])):
        for s in str:
            if i == len(s) or s[i]!=str[0][i]:
                return res
        res += str[0][i]
    return res

input_str_arr = ["flower","flow","flight"]
print("Longest Common Prefix : ",longest_common_prefix(input_str_arr))
print()
    





