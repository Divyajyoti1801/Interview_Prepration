"""
Problem Statement: Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

I/P: l1= {1,2,3,4,5}
     l2= {1,2,3}
O/P: 5
"""

def union_of_list(l1,l2):
    n = len(l1)
    m = len(l2)
    i = 0
    j = 0
    res = []
    
    while i<n and j<m:
        if(i>0 and l1[i]==l1[i-1]):
            i+=1
        elif(j>0 and l2[j]==l2[j-1]):
            j+=1
        elif(l1[i]<l2[j]):
            res.append(l1[i])
            i+=1
        elif(l1[i]>l2[j]):
            res.append(l2[j])
            j+=1
        else:
            res.append(l1[i])
            i+=1
            j+=1
    
    while i<n:
        if (i>0 and l1[i]!=l1[i-1]):
            res.append(l1[i])
        i+=1
    
    while j<m:
        if (j>0 and l2[j]!=l2[j-1]):
            res.append(l2[j])
        j+=1
    
    return res

print("Union Of The List: ",len(union_of_list([85,25,1,32,54,6],[85,2])))