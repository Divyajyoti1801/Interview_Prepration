"""
N-QUEENS-2

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
"""


def n_queens_2(n):
    res = 0
    col = set()
    posDiag = set()  # (r+c)
    negDiag = set()  # (r-c)

    def backtrack(r):
        if r == n:
            nonlocal res
            res += 1

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            backtrack(r+1)
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
    backtrack(0)
    return res


print("N-Queens-2 : ", n_queens_2(4))
