"""
Problem - 4: ROTATE MATRIX BY 90deg
    
Problem Statement:    
    - Given a square matrix of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space.

Input : N = 3 ; mtx[][] = [[1,2,3],[4,5,6],[7,8,9]]
Output : [[3,6,9],[2,5,8],[1,4,7]]

Idea : Transpose the matrix and Swap top and bottom element 
"""

def rotate_by_90deg(mtx):
    for i in range(len(mtx)):
        for j in range(i+1,len(mtx)):
            mtx[i][j],mtx[j][i] = mtx[j][i],mtx[i][j]
    
    for k in range(len(mtx)//2):
        for j in range(len(mtx)):
            mtx[k][j],mtx[len(mtx)-1-k][j]=mtx[len(mtx)-1-k][j],mtx[k][j]
    return mtx

input_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Rotated Matrix by 90deg: ",rotate_by_90deg(input_matrix))