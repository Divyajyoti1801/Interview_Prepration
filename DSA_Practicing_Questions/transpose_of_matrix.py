"""
Problem - 3 : TRANSPOSE OF MATRIX


Problem Statement:
    - Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.

I/P : N = 4 ; mat[][] = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
"""
def transpose_of_matrix(mtx):
    n = len(mtx)
    m = len(mtx[0])
    
    
    if(n!=m):
        return []

    for i in range(n):
        for j in range(i+1,m):
            mtx[i][j],mtx[j][i]= mtx[j][i],mtx[i][j]
    return mtx
input_matrix = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
print("Transpose of the Matrix: ",transpose_of_matrix(input_matrix))
