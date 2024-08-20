# A recursion to check palindrome in a strig
# Leetcode 125

# Method 1 basic while loop
def palin(s):
    s = s.lower()
    s = "".join(charc for charc in s if charc.isalnum())
    n = len(s)
    i = 0
    while(i < n/2):
        if(s[i] != s[n-i-1]):
            return False
        i = i + 1
    return True

#print(palin("121----"))

# Method 2 recursion
s = "check kcehc"
n = len(s)
def palin2(i):
    if(i >= n/2):
        return True;
    if(s[i] != s[n-i-1]):
        return False
    return palin2(i+1)

print(palin2(0))