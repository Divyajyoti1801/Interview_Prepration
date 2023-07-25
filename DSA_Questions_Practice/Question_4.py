"""
Problem Statement:
    - Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
I/P: arr = {0,2,1,2,0}
O/P: arr = {0,0,1,2,2}
"""
def Sort012(l):
    low = 0
    mid = 0
    high = len(l)-1
    
    while(mid<=high): 
        if l[mid] == 0:
            l[low],l[mid]=l[mid],l[low]
            low+=1
            mid+=1
        elif l[mid]==1:
            mid+=1
        else:
            l[mid],l[high]=l[high],l[mid]
            high-=1
    return l


print("List after sorting: ",Sort012([0,2,1,2,0]))
