"""
Problem - 7 : Plus One

Problem Statement : 
    - You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
    - Increment the large integer by one and return the resulting array of digits.
"""

def plus_one(digits=[]):
    # When last digits is less than 9
    if digits[-1] < 9:
        digits[-1]+=1
        return digits
    elif len(digits)==1 and digits[0] == 9:
        return [1,0]
    else:
        digits[-1] = 0
        digits[0:-1] = plus_one(digits[0:-1])
        return digits

print("Plus one solution: ",plus_one([1,2,3]))    

