import unittest

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = [[0]*(sum+1) for _ in range(N+1)]
        
        ## initialize dp
        for i in range(N+1):
            dp[i][0] = 1
            
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if j - arr[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j-arr[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][sum]
        
class Test(unittest.TestCase,Solution):
    def test_isSubsetSum(self):
        self.assertEqual(self.isSubsetSum(6,[3, 34, 4, 12, 5, 2],9),1)

if __name__ == '__main__':
    unittest.main()