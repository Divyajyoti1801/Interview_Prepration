"""
Problem - 2 : Roman to Integer

Problem Statement:
    - Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

Input: s = "III"
Output: 3
"""

def romanToInt(s):
    translation = {
        "I" :1,
        "V" : 5,
        "X" :10,
        "L":50,
        "C": 100,
        "D":500,
        "M" :1000
    }
    number = 0

    s = s.replace("IV","III").replace("IX","VIIII")
    s = s.replace("XL","XXXX").replace("IX","LXXXX")
    s = s.replace("CD","CCCC").replace("CM","DCCCC")
    
    for char in s:
        number += translation[char]
    return number