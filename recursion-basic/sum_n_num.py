# A basic recursion to get sum of first n numbers

# Method 1
def sum_n(i, sum):
    if(i < 1):
        print(sum)
        return
    sum_n(i-1, sum + i)

sum_n(10, 0)

# Method 2
def sum_n2(n):
    if(n == 0):
        return 0
    return n + sum_n2(n-1)

print(sum_n2(10))