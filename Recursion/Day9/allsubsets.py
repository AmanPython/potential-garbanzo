class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_sol = []
        N = len(nums)
        def helper_fun(arr,n):
            if n >= N:
                val = arr[:]
                val.sort()
                if val not in all_sol:
                    all_sol.append(val[:])
                return
            arr.append(nums[n])
            helper_fun(arr,n+1)
            arr.pop()
            helper_fun(arr,n+1)
        
        helper_fun([],0)
        return all_sol