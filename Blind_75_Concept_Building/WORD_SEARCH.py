"""
Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""


def word_search(board, word=""):
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        # Good Case
        if i == len(word):
            return True
        # Bad Case
        if (r < 0) or (c < 0) or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
            return False

        path.add((r, c))
        res = (dfs(r+1, c, i+1) or dfs(r-1, c, i +
                                       1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        path.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if (dfs(r, c, 0)):
                return True

    return False


print("Word Search : ", word_search([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))