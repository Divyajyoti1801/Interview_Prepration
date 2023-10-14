"""
BACKTRACKING ADVANCE
"""

"""
Concept of Backtracking - 1
    - Given a string print all those permutation which does not contain "AB" as a substring.

I/P : str = "ABC"
O/P : ["ACB","BAC","BCA","CBA"]

Backtracking Time Complexity  < O(n! * n)
"""
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

"""
Concept of Backtracking - 3
    - N Queen's Problem : The problem of placing N chess queens on an N*N chessboard so that no two queens attack each other.
    - Naive Solution : Generate all permutation of row number
    - Backtracking Solution : Cut down recursion tree as soon as we find infeasibility.
"""