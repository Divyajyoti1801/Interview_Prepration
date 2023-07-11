# DATA STRUCTURE
"""
List Introduction
    - Dynamic Size
    - Allows items of different types
"""

list_1=[10,20,30,40,50]
print(list_1)
print(list_1[3])
print(list_1[-1])
print(list_1[-2])

# Append function on list
list_1.append(30)
print(list_1)

# Insert function on list
list_1.insert(1,15)
print(list_1)

# Search function in list
print(15 in list_1)

# Count function in list
print(list_1.count(30))

# Index Checking of element in list
print(list_1.index(30)) # 1-form
print(list_1.index(30,4,7)) # 2-form 

# Removal of element in list
list_1.remove(20)
print(list_1)

# Removal of element from last
print(list_1.pop())
print(list_1)

# Removal from position
print(list_1.pop(3))
print(list_1)

# Delete item
del list_1[1]
print(list_1)

# Delete range of element in list
del list_1[0:2]
print(list_1)

list_2=[10,40,20,50]
print(list_2)

# Largest element of list
print(max(list_2))

# Smallest element of list 
print(min(list_2))

# Sum of all elements of the list 
print(sum(list_2))

# Reveres of list
list_2.reverse()
print(list_2)

# Sorting of list
list_2.sort()
print(list_2)


""""
Working Of List In Python

    Advantages
        - Random Access
        - Cache Friendly
        - Preallocated extra space
    
    Disadvantages
        - Insertion, Deletion  are slow
        - Search is also slow for unsorted.
        
How Does Dynamic Size Work?
    - Preallocate some extra space.
    - If becomes full, do the following.
        - Allocate a new space of larger size (multiply by x)
        - Copy old space to new
        - Free old space

Amortized Time
    - Initial Capacity: n
    - We double the size when become full 
    - Average Time to append (n+1) items = theta(1)
"""

# Average Or Mean Of A List 
"""
Problem Statement: Find the average of a mean of a list.

I/P : l = [10,20,30,40]
O/P : 25.0
"""
def mean_of_list(list_1):
    avg = sum(list_1) / len(list_1)
    return avg

print("Average Of a List: ",mean_of_list([30,60,40]))

# Separate Even And Odd
"""
Problem Statement: Separate even and odd from the list.

I/P : l = [10,41,30,15,80]
O/P : even = [10,30,80]
      odd = [41,15]
"""
def even_and_odd(list_1):
    even_list=[]
    odd_list=[]
    for i in list_1:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print("Even Element of the list: ", even_list)
    print("Odd Element of the list: ", odd_list)

even_and_odd([10,41,30,15,80])

"""
Problem Statement: get smaller elements from the list with respect to mentioned number

I/P : l = [8,100,20,40,3,7] x = 10
O/P : [8,3,7]
"""

def get_smaller_elements(list_1,x):
    result_list=[]
    list_1.sort()
    for i in list_1:
        if(i<x):
            result_list.append(i)
        
    return result_list

print(get_smaller_elements([8,100,20,40,3,7],10))