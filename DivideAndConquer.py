def BiCo(n, k):
 
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
 

    return BiCo(n-1, k-1) + BiCo(n-1, k)

n = 8
k = 3

print("The value of numbers " + str(n) +
               " and " + str(k) + " is",
               BiCo(n, k))
