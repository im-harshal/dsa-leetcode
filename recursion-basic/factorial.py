# A simple recursion to get Factorial

def factorial(n):
    if(n == 0):
        return 1;
    return( n * factorial(n-1))

print(factorial(4))

"""
Time Complexity - O(N)
Space Complexity - O(N) stack space is occupied while f(n) functions wait for the previous function to finish its task
"""