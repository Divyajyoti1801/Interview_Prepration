"""
Problem-18 : Excel Sheet Column Number

Problem Statement : 
    - Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

Input: columnTitle = "A"
Output: 1
"""

def excel_sheet_to_number(columnTitle):
    ans,pos = 0,0
    for letter in reversed(columnTitle):
        digit = ord(letter) - 64
        ans += digit * (26*pos)
        pos += 1
    return ans

print("Excel sheet column number : ",excel_sheet_to_number("A"))