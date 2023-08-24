"""
SEARCHING ADVANCE QUESTIONS
"""

"""
Search in an infinite sized Array
"""
def binary_search(arr,l,r,x):
    mid = (l+r)//2
    if r>=l:
        if arr[mid] == x:
            return mid
        if arr[mid]< x:
            return binary_search(arr,mid+1,r,x)
        return binary_search(arr,l,mid-1,x)
    return -1

def search_in_infinite(arr,key):
    l,h,val = 0,1,arr[0]
    while val<key:
        l = h
        h = 2*h
        val = arr[h]
    return binary_search(arr,l,h,key)
print("Search element in infinite search array: ",search_in_infinite([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170],10))
print()

"""
Search in a Sorted and Rotated Array
"""
def search_in_sorted_and_rotated(arr,x):
    n = len(arr)
    if n<0:
        return -1
    
    low = 0
    high = n - 1
    while(low<=high):
        mid = (low + high)//2
        if arr[mid] == x:
            return mid

        if arr[low]<=arr[mid]:
            if arr[low] <= x <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1 
print("Search in sorted and rotated array: ",search_in_sorted_and_rotated([100, 200, 400, 1000, 10, 20],10))
print()

"""
Find a peak element. 
"""
def peak_element(arr):
    n = len(arr)
    l = 0
    r = n - 1
    mid = 0

    while( l <= r):
        mid = ( l + r ) // 2

        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (arr[mid + 1] <= arr[mid]):
            break

        if(mid>0 and arr[mid-1] > arr[mid]):
            r = mid - 1
        else:
            l = mid + 1
    return mid
print("Index of a peak point is: ",peak_element([1, 3, 20, 4, 1, 0]))
print()

"""
Two Pointer Approach
"""
def two_pointer_approach(arr,x):
    i = 0
    j = len(arr) - 1
    while i<j:
        if arr[i] + arr[j] == x:
            return True
        elif arr[i] + arr[j] < x:
            i += 1
        else:
            j -= 1
    return False
print("Two pointer approach to find a pair whose sum: ",two_pointer_approach([2,5,8,12,30],17))
