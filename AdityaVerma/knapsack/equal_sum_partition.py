import unittest

class Solution:
    def equalPartition(self, N, arr,val=0):
        # code here
        if N == 0 and val == 0:
            return True 
        elif N == 0 and val != 0:
            return False
        return self.equalPartition(N-1,arr,val+arr[N-1]) or self.equalPartition(N-1,arr,val - arr[N-1])
    
class Test(unittest.TestCase,Solution):
    def test_equalPartition(self):
        self.assertTrue(self.equalPartition(4,[1, 5, 11, 5]))

if __name__ == '__main__':
    unittest.main()
    
