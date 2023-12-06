"""
SEARCH IN 2D MATRIX

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""
mtx = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3


def search_2D_matrix(mtx, target):
    ROWS, COLS = len(mtx), len(mtx[0])
    top, bot = 0, ROWS-1

    while top <= bot:
        row = top + ((bot-top)//2)
        if target > mtx[row][-1]:
            top = row + 1
        elif target < mtx[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False

    row = top+((bot-top)//2)
    l, r = 0, COLS-1
    while l <= r:
        m = l + ((r-l)//2)
        if target > mtx[row][m]:
            l = m + 1
        elif target < mtx[row][m]:
            r = m - 1
        else:
            return True
    return False


print("Search in 2D matrix : ", search_2D_matrix(mtx, target))
