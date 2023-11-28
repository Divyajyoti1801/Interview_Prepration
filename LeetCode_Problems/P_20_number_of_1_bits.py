"""
Problem - 20 : Number of 1 Bits

Problem Statement: 
    - Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""


def hamming_weights(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count


print("Hamming Weights: ", hamming_weights(1011))
