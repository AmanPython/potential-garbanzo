class Solution:
    def subsetSums(self, arr, N):
        all_sums = []  # List to store all subset sums
        
        def generate_subset_sums(current_sum, index):
            if index >= N:
                all_sums.append(current_sum)  # Add the current sum to the list of subset sums
                return 
            # Include the current element in the subset sum
            generate_subset_sums(current_sum + arr[index], index + 1)
            # Exclude the current element from the subset sum
            generate_subset_sums(current_sum, index + 1)
        
        generate_subset_sums(0, 0)  # Start the recursion with initial sum 0 and index 0
        return all_sums