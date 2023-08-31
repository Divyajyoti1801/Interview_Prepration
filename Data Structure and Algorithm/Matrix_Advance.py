"""
MATRIX ADVANCE: Primary Tool for Dynamic Programming
"""
mtx = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

"""
Problem Statement : Matrix in Sake Pattern
"""
def snake_pattern(mtx):
    row = len(mtx)
    col = len(mtx[0])
    
    for i in range(row):
        if i%2 == 0:
            for j in range(col):
                print(mtx[i][j],end = " ")
        else:
            for j in range(col-1,-1,-1):
                print(mtx[i][j],end=" ")
    print()
print("Traversing Matrix in Snake Pattern: ")
snake_pattern(mtx)
print()

"""
Problem Statement : Matrix Boundary Traversal 
"""
def boundary_traversal(mtx):
    row = len(mtx)
    col = len(mtx[0])
    
    if row == 1:
        print(*mtx[0],end = " ")
    elif col == 1:
        for i in range(row):
            print(mtx[i][0],end = " ")
    else:
        for i in range(col):
            print(mtx[0][i],end=" ")
        for i in range(1,row):
            print(mtx[i][col-1],end=" ")
        for i in range(col-2,-1,-1):
            print(mtx[row-1][i],end =" ")
        for i in range(row-2,0,-1):
            print(mtx[i][0],end=" ")
    print()
print("Boundary Traversal: ")
boundary_traversal(mtx)
print()

"""
Problem Statement: Transpose of a matrix
"""
def transpose_of_matrix(mtx):
    n = len(mtx)
    for i in range(n):
        for j in range(i,n):
            mtx[i][j],mtx[j][i] = mtx[j][i],mtx[i][j]
    
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            print(mtx[i][j],end =" ")
        print()
    print()
print("Transpose of the matrix: ")
transpose_of_matrix(mtx)
print()

"""
Problem Statement: Rotate matrix by 90deg 
"""
def rotate_by_90deg(mtx):
    n = len(mtx)
    for i in range(n):
        for j in range(i+1,n):
            mtx[i][j],mtx[j][i] = mtx[i][j],mtx[j][i]
    
    for i in range(n):
        low = 0
        high = n - 1
        while low<high:
            mtx[low][i],mtx[high][i] = mtx[high][i], mtx[low][i]
            low+=1
            high-=1
    
    for i in range(n):
        for j in range(n):
            print(mtx[i][j],end=" ")
        print()
print("Rotate Matrix by 90deg: ")
rotate_by_90deg(mtx)
print()

"""
Problem Statement: Spiral Traversal of a matrix
"""
def spiral_matrix(mtx):
    top = 0
    bottom = len(mtx) - 1
    left = 0
    right = len(mtx[0]) - 1
    while top <= bottom and left<=right:
        for i in range(left,right+1):
            print(mtx[top][i],end =" ")
        for i in range(top+1,bottom+1):
            print(mtx[i][right],end = " ")
        if top<bottom:
            for i in range(right-1,left-1,-1):
                print(mtx[bottom][i],end = " ")
        if left<right:
            for i in range(bottom-1,top,-1):
                print(mtx[i][left],end = " ")
        top+=1
        bottom-=1
        left+=1
        right-=1
    print()
print("Spiral Traversal of the matrix: ")
spiral_matrix(mtx)
print()

"""
Problem Statement: Search element in matrix which is row sorted and column sorted.
"""
mtx_2 =[[10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
def search_element_matrix(mtx_2,target):
    R = len(mtx_2)
    C = len(mtx_2[0])
    row,col = 0,C-1
    
    while row<R and col>=0:
        if mtx_2[row][col]==target:
            print("Found At: (", row ,",",col,")")
            return
        elif mtx_2[row][col] < target:
            row+=1
        else:
            col-=1
    print("Not Found")
print("Search Element in the matrix (row: sorted, col: sorted): ")
search_element_matrix(mtx_2,29)
print()

"""
Problem Statement: Median of a row-wise sorted matrix.
Time Complexity: O(log(mx-mn)*r*log(c))
"""
from bisect import bisect
def median_in_matrix(mtx):
    rows,cols = len(mtx),len(mtx[0])
    lo,hi = mtx[0][0],mtx[0][-1]
    
    for i in range(rows):
        lo = min(lo,mtx[i][0])
        hi = max(hi,mtx[i][-1])
    
    target_rank = (rows*cols+1) // 2
    while lo < hi: # type: ignore
        mid = (lo + hi) //2 # type: ignore
        count = 0
        for i in range(rows):
            count += bisect(mtx[i],mid)
        
        if count < target_rank:
            lo = mid + 1
        else:
            hi = mid
    return lo
mtx_3 = [[5,10,40],[1,2,3],[11,13,15]]
print("The Median of a row_sorted Matrix: ",median_in_matrix(mtx_2))
print()