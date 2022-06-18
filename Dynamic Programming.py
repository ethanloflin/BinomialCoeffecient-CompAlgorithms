def BiCo(n, k, dp):
     
    if dp[n][k] != -1:
        return dp[n][k]
 
    if k == 0:
        dp[n][k] = 1
        return dp[n][k]
     
    if k == n:
        dp[n][k] = 1
        return dp[n][k]
     
    dp[n][k] = (BiCo(n - 1, k - 1, dp) +
                BiCo(n - 1, k, dp))
                 
    return dp[n][k]
 
def BiCo2(n, k):
     
    dp = [ [ -1 for y in range(k + 1) ]
                for x in range(n + 1) ]
 
    return BiCo(n, k, dp)
 
n = 8
k = 3
 
print("The value of numbers " + str(n) +
               " and " + str(k) + " is",
               BiCo2(n, k))
