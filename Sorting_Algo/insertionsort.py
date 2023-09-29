def insertion_sort(arr):
    # Insertion sort for sorting individual buckets
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr, num_buckets=10):
    if len(arr) == 0:
        return arr

    # Find the minimum and maximum values in the input array
    min_val, max_val = min(arr), max(arr)
    
    # Calculate the range for each bucket
    bucket_range = (max_val - min_val + 1) / num_buckets

    # Create an empty list of buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets based on their value range
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Sort each bucket (insertion sort is used here, but other sorting algorithms can be used)
    for i in range(num_buckets):
        insertion_sort(buckets[i])

    # Concatenate sorted buckets to produce the final sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
