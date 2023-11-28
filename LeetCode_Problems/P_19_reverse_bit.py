"""
Problem - 19 : Reverse Bit

Problem Statement: 
    - Reverse bits of a given 32 bits unsigned integer.

    - Note:
        = Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""


def reverse_bit(n):
    res = 0
    for _ in range(32):
        res = (res >> 1) + (n & 1)
        n >>= 1
    return res
print("Reverse Bits : ", reverse_bit(11111111111111111111111111111101))