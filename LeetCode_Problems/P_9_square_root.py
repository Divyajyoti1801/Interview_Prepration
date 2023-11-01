"""
Problem - 9 : SQUARE ROOT OF THE NUMBER

Problem Statement : 
    - Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
    - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Input: x = 4
Output: 2
"""

def square_root(X):
    # using binary search
    low = 0
    high = X
    ans = -1
    while low<=high :
        mid = low +(high-low)//2
        
        if mid*mid == X:
            return mid
        elif(mid*mid< X):
            ans = mid
            low = mid+1
        else:
            high = mid - 1
    return ans
print("Square root of the number : ",square_root(16))