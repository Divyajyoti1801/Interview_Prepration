"""
Problem Statement: Move all negative numbers to beginning and positive to end with constant extra space

I/P: {-12,11,-13,-5,6,-7,5,-3,-6}
O/P: {-12,-13,-5,-7,-3,-6,11,6,5}
"""
def move_negative(l):
    j = 0
    for i in range(0,len(l)):
        if l[i] < 0:
            l[i],l[j] = l[j],l[i]
            j+=1
    return l
print("Moving Negative to Beginning: ",move_negative([-12,11,-13,-5,6,-7,5,-3,-6]))