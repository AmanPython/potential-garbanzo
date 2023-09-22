class Solution:
	def subsetSums(self, arr, N):
		# code here
		all_sol = []
		def helper_fun(totalsum,n):
			if n >= N:
				all_sol.append(totalsum)
				return 
			helper_fun(totalsum + arr[n],n+1)
			helper_fun(totalsum,n+1)
		helper_fun(0,0)
		return all_sol
	
	