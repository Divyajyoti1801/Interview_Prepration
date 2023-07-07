""" 

MATHEMATICS FOR DATA STRUCTURE AND ALGORITHM

"""

# SUM OF NATURAL NUMBERS
"""
Problem Statement: Find total money saved after 10 days.
Day 1: 1
Day 2: 2
Day 3: 3 ..... n days: n
"""
def sum_of_natural_numbers(n):
    return (n * (n+1))/2
# time complexity: O(1)
print(sum_of_natural_numbers(10))


# COUNT OF DIGITS
"""
Problem Statement: Find the numbers of digit present in the particular number.

I/P : x = 9253
O/P : 4

"""
def count_of_digits(x):
    count=0
    while x > 0:
       x//=10  #floor division
       count+=1
    return count
# time complexity: O(n)
print(count_of_digits(9253))

# PALINDROME NUMBER
"""
Problem Statement: check if the number i palindrome or not.
"""
def check_palindrome(n):
    rem=0
    org=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10 + rem
        n//=10
    if rev == org:
        return True
    return  False
# time complexity: O(n)
print(check_palindrome(78987))

# FACTORIAL OF THE NUMBER
"""
Problem Statement: Find factorial of the number
"""
def factorial_number(n):
    if n==0:
        return 1
    return n*factorial_number(n-1);
# time complexity: O(n)
print(factorial_number(5))

# COUNT TRAILING ZEROES IN FACTORIAL
"""
Problem Statement: Count trailing zeroes in factorial.

I/P: n = 5
O/P: n = 1

Concept:
    Trailing Zero Count: [n/5] + [n/25] + [n/125] + .....
"""
def trailing_zeroes(n):
    res=0
    i=5
    while(i<=n):
        res=res+(n//i)
        i*=5
    return res
# time complexity: theta(log(n))

# GREATEST COMMON DIVISOR
"""
Problem Statement: find highest common factor or greatest common divisor of the number.
"""
def GCD(a,b):
   if(b==0):
       return a
   return GCD(b,a%b);
# time complexity: O(n)
print(GCD(4,6))

# LEAST COMMON MULTIPLE
"""
Problem Statement: find least common multiple of two numbers.
"""
def LCM(a,b):
    return a * b //  GCD(a,b);
print(LCM(12,15))

# PRIME NUMBER
"""
Problem Statement: Check for Prime Number
"""
def check_prime_number(n):
    if(n==1):
        return False
    if n==2 or n==3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while(i * i <= n):
        if(n % i == 0  or n % (i+2) == 0 ):
            return False
        i+=6
    return True
print(check_prime_number(14))

# Prime Factorization
"""
Problem Statement: Find prime factors of the number.
"""
def prime_factors(n):
    for i in range(2,n+1):
        if check_prime_number(i):
            x=i
            while n%x==0:
                print(i)
                x*=i;
print(prime_factors(100))

# ALL DIVISOR OF A NUMBER
"""
Problem Statement: Find all divisor of a given number.

Efficient Solution Algo:
    - Divisor always appear in pairs
        30: (1,30), (2,15), (3,10), (5,6)
    - One of the divisor in every pair is smaller than or equal to sqrt(n)
        for a pair (x,y)
            - X * Y = n
            let x be the smaller x <= y
            x * x <= n  
            x <= sqrt(n)  
"""
def   divisor_of_number(n):
    i=1 
    while( i * i <=n):
        if( n % i == 0):
            print(i)
            if(i!=(n/i)):
                print(n/i)
        i+=1
# Time Complexity: theta(n^(1/2))

# SIEVE OF ERATOSTHENES
"""
Problem Statement: Find prime numbers until that  number.
"""
def sieve_of_eratosthenes(num):
    if num<=1:
        return
    prime = [True for i in range(num+1)]
    p=2
    while(p * p <= num):
        if(prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] =  False
        p += 1
    
    for p in range(2, num+1):
        if prime[p]:
            print(p)
# Time Complexity: O(n log(log(n)))
print(sieve_of_eratosthenes(20))

# COMPUTING POWER
"""
Problem Statement: compute the power of given number.
I/P: x=2 , n=3
O/P: x=3 , n=4
"""
def computing_power(x,n):
    if (n==0):
        return 1
    temp = 0
    temp = computing_power(x,int(n/2))
    if(n % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp
# Time Complexity: O(log(n))
print(computing_power(2,3))

# Iterative Power
"""
Problem Statement: Computer power of a given number with the help iterative power.

Concept:
    - Every number can be written as sum of powers of 2, for example: 19 = 16 + 2 + 1
    - We can traverse through all bits of a numbers (LSB to MSB) in O(log n)
    - Lowest Significant Bit
    - Most Significant Bit
"""
def binary_method(x,n):
    res = 1
    while n > 0:
        if (n % 2 != 0):
            res *= x
        x *= x
        n //= 2
    return res
"""
if modulo is given:

def binary_method(x,n,m):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * x) % m
        x = (x * x) % m
        n = n >> 1
    return res
"""
# Time Complexity: O(log(n))
print(binary_method(2,3))
