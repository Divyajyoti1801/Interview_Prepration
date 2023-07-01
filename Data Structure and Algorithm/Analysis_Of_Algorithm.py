"""
Analysis of Algorithm

"""

# solution 1
def sum_of_natural_numbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    
    print(sum)
sum_of_natural_numbers(10)
#order of growth: C2n + C3 (linear growth)

#solution 2
def sum_of_natural_numbers_2(n):
    return n*(n+1)/2
#order of growth: C1 (no growth)

#solution 3
def sum_of_natural_numbers_3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+j
    
    return sum
#order of growth: C4(n^2) + C5n + C6 (quadratically growth)
"""
Asymptotic Analysis (Theoretical Analysis):
    - No dependency on machine programming language etc.
    - We do not have to implement all ideas/algorithm.
    - Asymptotic Analysis is about measuring order of growth in terms of input size.
"""