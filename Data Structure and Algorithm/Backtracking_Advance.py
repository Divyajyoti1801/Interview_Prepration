"""
BACKTRACKING ADVANCE
"""

"""
Concept of Backtracking - 1
    - Given a string print all those permutation which does not contain "AB" as a substring.

I/P : str = "ABC"
O/P : ["ACB","BAC","BCA","CBA"]
"""
def is_safe(str,l,i,r):
    if(l!= 0 and str[l-1]=="A" and str[i] == "B"):
        return False
    if(r == l+1 and str[i] == "A" and str[l] == "B"):
        return False
    return True

def permutation_of_string(str,l,r):
    if(l==r):
        print(*str,sep="",end=" ")
        return
    else:
        for i in range(l,r+1):
            if(is_safe(str,l,i,r)):
                str[i],str[l] = str[l],str[i]
                permutation_of_string(str,l+1,r)
                str[i],str[l] = str[l],str[i]
print("Permutation of a string : ")
permutation_of_string(list("ABC"),0,len("ABC")-1)
print()