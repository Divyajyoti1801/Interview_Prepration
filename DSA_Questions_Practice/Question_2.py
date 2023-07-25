"""
Problem Statement: Find maximum and minimum from the list.

I/P: {3,5,4,1,9}
O/P: max = 9, min = 1
"""
def max_min_list(l):
    if len(l) <=0:
        return -1,-1
    return max(l),min(l)

mx,mn=max_min_list([22,14,8,17,35,3])
print("Maximum of the list: ",mx)
print("Minimum of the list: ",mn)