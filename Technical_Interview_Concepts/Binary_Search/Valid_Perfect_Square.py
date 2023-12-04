"""
VALID PERFECT SQUARE

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
"""


# Most-Efficient time complexity : O(sqrt(n))

def valid_perfect_square_efficient(num):
    for i in range(1, num+1):
        if i*i == num:
            return True

        if i*i > num:
            return False
# Binary-Search based solution


def valid_perfect_square(num):
    low = 1
    high = num

    while low <= high:
        mid = low + ((high-low)//2)
        if mid*mid == num:
            return True
        elif mid*mid < num:
            low = mid + 1
        else:
            high = mid - 1

    return False


print("Valid perfect square : ", valid_perfect_square(9))
print("Valid perfect square : ", valid_perfect_square_efficient(16))
