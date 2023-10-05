from typing import List

def backtrack(arr,k,ind,dp):
    if ind == 0 and k != 0:
        return 0
    if k == 0:
        return 1
    if dp[ind][k] != -1:
        return dp[ind][k]
    if k - arr[ind-1] >= 0:
        dp[ind][k] = backtrack(arr,k-arr[ind-1],ind-1,dp) + backtrack(arr,k,ind-1,dp)
        return dp[ind][k]
    else:
        dp[ind][k] = backtrack(arr,k,ind-1,dp)
        return dp[ind][k]


def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    dp = [[-1]*(k+1) for _ in range(n+1)]
    ## initialize the base condition
    for i in range(k+1):
        dp[0][i] = 0
    for j in range(n+1):
        dp[j][0] = 1

    for i in range(1,k+1):
        for j in range(1,n+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][k]