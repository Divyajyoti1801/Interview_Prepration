"""
HASHING ADVANCE PROBLEMS & CONCEPTS
"""

"""
Problem Statement : Intersection of Two Arrays
"""
def intersection_of_two_arrays_1(arr1, arr2):
    res = 0
    for i in range(len(arr1)):
        flag = False
        for j in range(i-1):
            if arr1[j] == arr1[i]:
                flag = True
                break
        if flag == True:
            continue
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                res += 1
                break
    return res
print("Intersection of Two Arrays (Naive) O(m * (m+n)): ",
      intersection_of_two_arrays_1([10, 15, 20, 15, 30, 30, 5], [30, 5, 30, 80]))
"""
Algorithm for Efficient solution:
    - Solution-1:
        = Insert all elements of a[] in a set
        = Insert all element of b[] in a set
        = Now Traverse through set_a and increment count for elements that are present in set_b also.
    
    - Solution-2: 
        = Insert all elements of a[] in a set
        = Traverse through b[]. Search for every element b[i] in set_a. if present
            - Increment res
            - Remove b[i] from set_a
"""
def intersection_of_two_arrays_2(arr1, arr2):
    set_a = set()
    for i in range(len(arr1)):
        set_a.add(arr1[i])
    res = 0
    for i in range(len(arr2)):
        if arr2[i] in set_a:
            res+=1
            set_a.remove(arr2[i])
    return res
print("Intersection of Two Arrays (Efficient) (O(m+n)): ",intersection_of_two_arrays_2([10, 15, 20, 15, 30, 30, 5], [30, 5, 30, 80]))
print()

"""
Problem Statement: Union of two unsorted arrays
"""
def union_two_unsorted_arrays_1(arr1,arr2):
    res = 0
    c = [0]*(len(arr1)+len(arr2))
    for i in range(len(arr1)):
        c[i] = arr1[i]
    for i in range(len(arr2)):
        c[i] = arr2[i]
    for i in range(len(arr1)+len(arr2)):
        flag = False
        for j in range(i):
            if c[i] == c[j]:
                flag = True
                break
        if flag == False:
            res += 1
    return res
print("union of two unsorted arrays (Naive) O((m+n)*(m+n)): ",union_two_unsorted_arrays_1([10,12,15],[18,12]))
def union_two_unsorted_arrays_2(arr1,arr2):
    res_set = set()
    for i in arr1:
        res_set.add(i)
    for j in arr2:
        res_set.add(j)
    return len(res_set)
print("Union of two unsorted arrays (Efficient) (O(m+n)): ",union_two_unsorted_arrays_2([10,12,15],[18,12]))
print()

"""
Problem Statement: Pair with given sum
"""
def pair_with_given_sum_1(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j] == sum):
                return True
    return False
print("Pair with given sum (Naive) O(n^2): ",pair_with_given_sum_1([3,2,8,15,-8],17))
def pair_with_given_sum_2(arr,sum):
    set_res = set()
    for i in arr:
        if (sum-i) in set_res:
            return True
        set_res.add(i)
    return False
print("Pair with given sum (Efficient): ",pair_with_given_sum_2([3,2,8,15,-8],17))
print()

"""
Problem Statement: Subarray with 0 sum
"""
def subarray_with_zero_sum_1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(arr[i:j])==0:
                return True
    return False
print("Subarray with 0 sum (Naive) O(n^2): ",subarray_with_zero_sum_1([4,3,-2,1,1]))
"""
Efficient Solution:
    - Using PrefixSum & Hashing together
"""
def subarray_with_zero_sum_2(arr):
    pre_sum = 0
    h = set()
    for i in range(len(arr)):
        pre_sum += arr[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False
print("Subarray with 0 sum (Efficient) O(n): ",subarray_with_zero_sum_2([4,3,-2,1,1]))
print()

"""
Problem Statement: Subarray with given sum (There are no negative elements in the array)
"""
def subarray_with_given_sum_1(arr,sum):
    for i in range(len(arr)):
        curr=0
        for j in range(i,len(arr)):
            curr += arr[j]
            if curr==sum:
                return True
    return False
print("Subarray with a given sum (Naive) O(n^2): ",subarray_with_given_sum_1([1,4,20,3,10,5],33))
"""
Efficient Solution: 
    - We use window sliding technique with a window of variable size
"""
def subarray_with_given_sum_2(arr,sum):
    s,curr = 0,0
    for e in range(len(arr)):
        curr += arr[e]
        while curr>sum:
            curr-=arr[s]
            s+=1
        if curr == sum:
            return True
    return False
print("Subarray with a given sum (Efficient) O(n): ",subarray_with_given_sum_2([1,4,20,3,10,5],33))
print()

"""
Problem Statement: Check for Palindrome Permutation
Efficient Solution:
    - Answer is going to be true if there is at most one character with odd frequency
    - Else False
"""
from collections import Counter
def palindrome_permutation(S):
    cnt = Counter(S)
    odd = 0
    for freq in cnt.values():
        if freq%2!=0:
            odd+=1
            if odd > 1:
                return False
    return True
print("Check for palindrome permutation (Efficient) O(n): ",palindrome_permutation("geegg"))
print()

"""
Problem Statement: Longest subarray with given sum
"""
def longest_subarray_with_sum_1(arr,sum):
    n = len(arr)
    res = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += arr[j]
            if curr_sum == sum:
                res = max(res,j-i+1)
    return res
print("Longest subarray with the given sum (Naive) : ",longest_subarray_with_sum_1([5,8,-4,-4,9,-2,2],0))
def longest_subarray_with_sum_2(arr,sum):
    n = len(arr)
    res_dict = dict()
    pre_sum = 0
    res = 0
    for i in range(n):
        pre_sum += arr[i]
        if pre_sum == sum:
            res = i+1
        if pre_sum not in res_dict:
            res_dict[pre_sum] = i
        if pre_sum-sum in res_dict:
            res = max(res,i-res_dict[pre_sum-sum])
    return res 
print("Longest subarray with the given sum (Efficient): ",longest_subarray_with_sum_2([5,8,-4,-4,9,-2,2],0))
print()

"""
Problem Statement: Longest subarray with equal number of zero and one
"""
def longest_subarray_equal_zero_one_1(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        c_0 = 0
        c_1 = 1
        for j in range(1,n):
            if arr[j]==0:
                c_0+=1
            else:
                c_1+=1
            if c_0 == c_1:
                res = max(res,j-i+1)
    return res
print("Longest subarray with equal zero and one (Naive): ",longest_subarray_equal_zero_one_1([1,0,1,1,1,0,0]))
def longest_subarray_equal_zero_one_2(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1 # 0 will be converted into -1 to use longest 0 sum subarray
    res_dict = dict()
    sum = 0
    max_len = 0
    for i in range(n):
        sum  += arr[i]
        if sum == 0:
            max_len = i + 1
        if sum in res_dict:
            max_len = max(max_len,i-res_dict[sum])
        else:
            res_dict[sum] = i
    return max_len
print("Longest subarray with equal zero and one (Efficient): ",longest_subarray_equal_zero_one_2([1,0,1,1,1,0,0]))
print()

"""
Problem Statement: Longest common span with same sum in binary Array
"""
def longest_common_span_binary_1(arr1,arr2):
    res = 0
    n = len(arr1)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(i,n):
            sum1+=arr1[i]
            sum2+=arr2[i]
            if sum1 == sum2:
                res =max(res,j-i+1)
    return res
print("Longest common span with same sum in Binary (Naive): ",longest_common_span_binary_1([0,1,0,0,0,0],[1,0,1,0,0,1]))
"""
Efficient Solution: The problem is going to reduce into the problem of longest subarray with zero sum in array
"""
def longest_common_span_binary_2(arr1,arr2):
    n = len(arr1)
    arr = [0]*n
    for i in range(n):
        arr[i] = arr1[i] - arr2[i] # Storing difference of elements of different arrays
    res_dict = dict()
    sum = 0
    max_len = 0
    for i in range(n): # longest subarray with zero sum
        sum+=arr[i]
        if sum == 0:
            max_len = i + 1
        if sum in res_dict:
            max_len = max(max_len,i-res_dict[sum])
        else:
            res_dict[sum] = i
    return max_len
print("Longest common span with same sum in Binary (Efficient) (O(n)): ",longest_common_span_binary_2([0, 1, 0, 0, 0, 0],[1, 0, 1, 0, 0, 1]))
print()

"""
Problem Statement : Longest consecutive subsequence
"""
def longest_consecutive_subsequence_1(arr):
    n = len(arr)
    arr.sort()
    res = 1
    curr = 1
    for i in range(1,n):
        if arr[i] == arr[i-1]+1:
            curr += 1
        else:
            res = max(res,curr)
            curr = 1
    res = max(res,curr)
    return res
print("Longest consecutive subsequence (Naive): ",longest_consecutive_subsequence_1([1,9,3,4,2,10,13]))
"""
Efficient Method: 
    - We first insert all elements in a hash table
    - Then with 2n lookups, we find the result
"""
def longest_consecutive_subsequence_2(arr):
    s = set()
    res = 0
    for i in arr:
        s.add(i)
    for i in arr:
        if i-1 not in s:
            curr = 1
            while curr + i in s:
                curr+=1
            res = max(res,curr)
    return res
print("Longest consecutive subsequence (Efficient) O(n): ",longest_consecutive_subsequence_2([1,9,3,4,2,10,13]))
print()

"""
Problem Statement: Count distinct elements in every window  
Idea of Naive Solution:
    - There will (n-k+1) windows
    - Traverse through every window and count distinct elements in it.
    - Mainly using nested loops
Idea of Efficient Solution:
    - The idea is to use count of previous window to get the current count
"""
def count_distinct_element_window_1(arr,k):
    res = []
    for i in range(len(arr)-k+1):
        res.append(len(set(arr[i:i+k])))
    return res
print("Count distinct element in every window(Naive): ",count_distinct_element_window_1([10,20,20,10,30,40,10],4))
def count_distinct_element_window_2(arr,k):
    result = []
    res = Counter(arr[0:k])
    result.append(len(res))
    for i in range(k,len(arr)):
        x = arr[i-k]
        res[x] -= 1
        res[arr[i]] += 1
        if res[x] == 0:
            del res[x]
        result.append(len(res))
    return result
print("Count distinct element in every window(Efficient): ",count_distinct_element_window_2([10,20,20,10,30,40,10],4))
print()

"""
Problem Statement : More than n/k occurrences
"""
def more_than_n_by_k_1(arr,k):
    res = []
    arr.sort()
    i = 1
    count = 1
    n = len(arr)
    while i < len(arr):
        while i<len(arr) and arr[i] == arr[i-1]:
            count += 1
            i+=1
        if count > n//k:
            res.append(arr[i-1])
        count = 1
        i+=1
    return res
print("More than n/k occurrences(Naive): ",more_than_n_by_k_1([30,10,20,20,10,20,30,30],4))
def more_than_n_by_k_2(arr,k):
    res = []
    n = len(arr)
    c = Counter(arr)
    for x in c:
        if c[x] > n//k:
            res.append(x)
    return res
print("More than n/k occurrences (Efficient): ",more_than_n_by_k_2([30,10,20,20,10,20,30,30],4))