"""
Problem - 5 : TOWER OF HANOI

Problem Statement: 
    - The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.
    - Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.

I/P : N = 2
O/P :
    move disk 1 from rod 1 to rod 2
    move disk 2 from rod 1 to rod 3
    move disk 1 from rod 2 to rod 3
"""

def tower_of_hanoi(N,source,helper ,destination):
    if N==1:
        print("move disk ",N," from rod ",source," to ",destination)
        return 1
    count = tower_of_hanoi(N-1,source,destination,helper)
    print("move disk ",N," from rod ",source," to ",destination)
    count+=tower_of_hanoi(N-1,helper,source,destination) # type: ignore
    return count+1
print("Tower of Hanoi: ")
print(tower_of_hanoi(3,1,2,3))