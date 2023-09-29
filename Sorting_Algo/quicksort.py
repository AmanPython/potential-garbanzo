def quicksort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr)//2]  # middle element
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([3,2,1]))
