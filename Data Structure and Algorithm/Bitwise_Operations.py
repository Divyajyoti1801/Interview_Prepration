"""
BITWISE OPERATIONS
"""

"""
Binary Representation of negative number 
    - represented in 2's compliment form 
    - Range of Numbers: [-2^(n-1) to 2^(n-1)-1] here n is the number of bits
    - Steps to get 2's compliment 
        = Invert all bits
        = Add 1
    - Direct formula: 2^n - x

Why 2's Complement Form?
    - We have only one representation of zero
    - The arithmetic operations are easier to perform. Actually 2's compliment form is derived from the idea of 0 - x
    - The leading bit is always 1
"""

"""
Bitwise Operation Implementation
"""
print("Binary representation of 18: ",bin(18))
print("Binary representation of 12: ",bin(12))
print("Binary to decimal: ",int("0b10010",2))
print("Binary to decimal: ",int("0b1100",2))
print("AND Operation: ",3 & 6)
print("OR Operation: ",3 | 6)
print("XOR Operation: ",3 ^ 6)
print("Left Shift Operation: ",5<<1)
print("Right Shift Operation: ",5>>1)
print("Bitwise Not Operation: ",~5)
print()
"""
Problem Statement: Check the kth bit is set or not
I/P: n = 5, k = 1
O/P: Yes
"""
def Kth_BitSet(n,k):
    if n & (1 << (k-1)):
        print("Yes")
    else:
        print("Not Set")

"""
Problem Statement: Count Set Bits
I/P: n=5
O/P: 2

Naive Algorithm:
    - LSB: Least Significant Bit
    - MSB: Most Significant Bit
    - Initialize: res = 0
    - Traverse through all bits from LSB to MSB and increment res for set bits
    - Return res
    - Time Complexity: O(No. of Bits)

Efficient Algorithm: Brian Kernigam's Algorithm
    - Idea : Traverse only through Set Bits
"""
def naive_count_set_bits(n):
    res = 0
    while n:
        res = res + (n & 1)
        n = n // 2
    return res
print("Count Set Bits (Naive): ",naive_count_set_bits(5))

def count_set_bits_BK(n):
    res = 0
    while n:
        n = n & (n-1)
        res += 1
    return res
print("Count Set Bits (Brian Kernigam): ",count_set_bits_BK(5))
print()
"""
Problem Statement: Find the only odd
"""
def only_odd(l=[]):
    res = 0
    for x in l:
        res ^= x
    return res
print("The only Odd in the lis: ",only_odd([10,30,30,10,30,30,20]))
print()

"""
Problem Statement: Power of 2
"""
def power_of_two(n):
    if n == 0:
        return False
    return (n & (n-1) == 0)
print("The is the number power of 2: ",power_of_two(4))
print()

"""
Problem Statement: Find Only one odd occurring
I/P: [4,2,4,4,4,5,5]
O/P: 3
    Time Complexity: O(n(2^n))
"""
def one_odd_occurring(l=[]):
    res = 0
    for i in l:
        res = res ^ i
    return res
print("The only odd occurring number: ",one_odd_occurring([4,3,4,4,4,5,5,3,3]))
print()

"""
Problem Statement: Find two odd occurring elements
I/P: arr = [3,4,3,4,5,4,4,6,7,7]
O/P: 5 6
"""
def two_odd_occurring(l = []):
    xors = 0
    res1 = 0
    res2 = 0
    
    for i in l:
        xors = xors ^ i
    
    sn = xors & ~(xors-1)
    for i in l:
        if i & sn!=0:
            res1 ^= i
        else:
            res2^=i
    print(res1,res2)
print("The two odd occurring elements: ")
two_odd_occurring([3,4,3,4,5,4,4,6,7,7]);
print()

"""
Problem Statement: Power set using Bit wise operator
I/P: s = "abc", n = 3
    - We consider binary representation of number from 0 to 7
"""
def print_power_set(s):
    n = len(s)
    pSize = 1 << n
    for i in range(pSize):
        for j in range(n):
            if((i & (1<<j))!=0):
                print(s[j],end=" ")
        print()
print("Printing Power set: ")
print_power_set("abc")
print()