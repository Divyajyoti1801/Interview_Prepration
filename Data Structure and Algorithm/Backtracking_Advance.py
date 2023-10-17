"""
BACKTRACKING ADVANCE
"""
import math

"""
Concept of Backtracking - 1
    - Given a string print all those permutation which does not contain "AB" as a substring.

I/P : str = "ABC"
O/P : ["ACB","BAC","BCA","CBA"]

Backtracking Time Complexity  < O(n! * n)
"""
from re import L


def permutation_of_string_naive(str,l,r):
    if l == r:
        if "AB" not in ''.join(str):
            print(*str,sep="",end=" ")
        return
    else:
        for i in range(l,r+1):
            str[i],str[l]=str[l],str[i]
            permutation_of_string_naive(str,l+1,r)
            str[i],str[l] = str[l],str[i]
print("Permutation of the string (Naive): ")
permutation_of_string_naive(list("ABC"),0,len("ABC")-1)
print()
def is_safe(str,l,i,r):
    if(l!= 0 and str[l-1]=="A" and str[i] == "B"):
        return False
    if(r == l+1 and str[i] == "A" and str[l] == "B"):
        return False
    return True

def permutation_of_string(str,l,r):
    if(l==r):
        print(*str,sep="",end=" ")
        return
    else:
        for i in range(l,r+1):
            if(is_safe(str,l,i,r)):
                str[i],str[l] = str[l],str[i]
                permutation_of_string(str,l+1,r)
                str[i],str[l] = str[l],str[i]
print("Permutation of a string : ")
permutation_of_string(list("ABC"),0,len("ABC")-1)
print("\n")

"""
Concept of Backtracking - 2
    - Rat in the Maze
    - Only two moved are allowed from i to j
        = (i+1,j)
        = (i,j+1)
    - I/P : maze[][] = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
"""
rat_maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
def print_maze_solution(sol):
    N = len(rat_maze)
    for i in range(N):
        for j in range(N):
            print(sol[i][j],end=" ")
        print()
def is_safe_maze(maze,i,j):
    return i<len(maze) and j<len(maze) and maze[i][j]==1
def solve_maze_problem(maze):
    N = len(maze)
    sol =[[0 for j in range(N)] for i in range(N)]
    
    if solve_maze_problem_utility(maze,0,0,sol) == False:
        print("Solution Doesn't exists!")
        return False
    print_maze_solution(sol)
    return True
def solve_maze_problem_utility(maze,i,j,sol):
    if i == len(maze)-1 and j == len(maze)-1 and maze[i][j] == 1:
        sol[i][j] = 1
        return True
    
    if is_safe_maze(maze,i,j) == True:
        sol[i][j] = 1
        if solve_maze_problem_utility(maze,i+1,j,sol) == True:
            return True
        if solve_maze_problem_utility(maze,i,j+1,sol) == True:
            return True
        sol[i][j] = 0
    return False
print("RAT MAZE PROBLEM SOLUTION")
print("MAZE as input")
for i in range(len(rat_maze)):
    for j in range(len(rat_maze)):
        print(rat_maze[i][j],end = " ")
    print()
print("Solution of Rat Maze: ")
solve_maze_problem(rat_maze)
print()
"""
Concept of Backtracking - 3
    - N Queen's Problem : The problem of placing N chess queens on an N*N chessboard so that no two queens attack each other.
    - Naive Solution : Generate all permutation of row number
    - Backtracking Solution : Cut down recursion tree as soon as we find infeasibility.
"""
N_Queens_Board = [[False for i in range(3)] for i in range(3)]
def N_Queens_Safe(row,col):
    for i in range(col):
        if N_Queens_Board[row][i]:
            return False
        i,j = row,col
        while i>=0 and j>=0:
            if N_Queens_Board[i][j]:
                return False
            i-=1
            j-=1
        i,j=row,col
        while i<3 and j<0:
            if N_Queens_Board[i][j]:
                return False
            i+=1
            j-=1
    return True
def N_Queens_Sol():
    if N_Queens_utility(0) == False:
        return False
    print(N_Queens_Board)
    return False

def N_Queens_utility(col):
    if col == 3:
        return True
    for i in range(3):
        if N_Queens_Safe(i,col):
            N_Queens_Board[i][col] = True
            if N_Queens_utility(col+1):
                return True
            N_Queens_Board[i][col] = False
    return False
print("N-Queens Problem : ")
N_Queens_Sol()
print()

"""
Concept of Backtracking - 4
    - Sudoku Problem
    - Rules:
        = Distinct Rows
        = Distinct Columns
        = Sub-Matrix Distinct
"""
def sudoku_safe(board,row,col,num):
    N = len(board)
    for d in range(N):
        if board[row][d] == num:
            return False
    
    for r in range(N):
        if board[r][col] == num:
            return False
    s = int(math.sqrt(N))
    box_row_start = row - row%s
    box_col_start = col - col%s
    
    for r in range(box_row_start,box_row_start+s):
        for d in range(box_col_start,box_col_start+s):
            if board[r][d] == num:
                return False
    return True

def sudoku_sol(board):
    N = len(board)
    row = -1
    col = -1
    isEmpty = True
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                row = i
                col = j
                isEmpty = False
                break
        if not isEmpty:
            break
    if isEmpty:
        return True
    for num in range(1,N+1):
        if sudoku_safe(board,row,col,num):
            board[row][col] = num
            if sudoku_sol(board):
                return True
            else:
                board[row][col] = 0
    return False
sudoku_board = [[1,0,3,0],[0,0,2,1],[0,1,0,2],[2,4,0,0]]
sudoku_sol(sudoku_board)
print("Sudoku Problem : ",sudoku_board)
print()
