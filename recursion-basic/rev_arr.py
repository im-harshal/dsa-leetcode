# A simple recursion to reverse an array 
a = [1,2,3,4,5]
print(a)

# Method 1
def rev_arr(l, r):
    if(l >= r):
        return
    
    #swap logic
    temp = a[r]
    a[r] = a[l]
    a[l] = temp

    return rev_arr(l+1, r-1)

rev_arr(0,4)
print(a)