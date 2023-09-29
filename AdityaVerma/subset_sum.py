import unittest

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        # Recursive Solution
        if sum == 0:
            return True
        elif N == 0 and sum != 0:
            return False
        if sum - arr[N-1] >= 0:
            return self.isSubsetSum(N-1,arr,sum-arr[N-1]) or self.isSubsetSum(N-1,arr,sum)
        else:
            return self.isSubsetSum(N-1,arr,sum)
        

class Test(unittest.TestCase,Solution):
    def test_isSubsetSum(self):
        self.assertEqual(self.isSubsetSum(6,[3, 34, 4, 12, 5, 2],9),1)

if __name__ == '__main__':
    unittest.main()