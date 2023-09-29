class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_subsets = []  # List to store all subsets
        
        N = len(nums)
        
        def generate_subsets(current_subset, index):
            if index >= N:
                # Sort the current subset and check if it's not already in the result list
                sorted_subset = sorted(current_subset)
                if sorted_subset not in all_subsets:
                    all_subsets.append(sorted_subset[:])
                return
            
            # Include the current element in the subset
            current_subset.append(nums[index])
            generate_subsets(current_subset, index + 1)
            
            # Exclude the current element from the subset
            current_subset.pop()
            generate_subsets(current_subset, index + 1)
        
        generate_subsets([], 0)  # Start the recursion with an empty subset and index 0
        return all_subsets
