import unittest

class Solution:
    def helperFun(self,N,arr,sum,dp):
        if sum == 0:
            return True
        elif N == 0 and sum != 0:
            return False
        if dp[sum][N] != -1:
            return dp[sum][N]
        if sum - arr[N-1] >= 0:
            dp[sum][N] = self.helperFun(N-1,arr,sum-arr[N-1],dp) or self.helperFun(N-1,arr,sum,dp)
            return dp[sum][N]
        else:
            dp[sum][N] = self.helperFun(N-1,arr,sum,dp)
            return dp[sum][N]
    def isSubsetSum (self, N, arr, sum):
        # code here 
        ## Initialize DP
        dp = [[-1]*(N+1) for _ in range(sum+1)]
        ## Initialize the initial value
        for i in range(sum+1):
            dp[i][0] = True
        self.helperFun(N,arr,sum,dp)
        return dp[sum][N]
    
