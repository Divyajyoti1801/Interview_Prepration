"""
Sum Of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Input: a = 1, b = 2
Output: 3
"""


def sum_of_two_integers(a=0, b=0):
    mask = 0xfffffff

    while (b & mask) > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return (a & mask) if b > 0 else a


print("Sum Of Two Integers : ", sum_of_two_integers(1, 2))
