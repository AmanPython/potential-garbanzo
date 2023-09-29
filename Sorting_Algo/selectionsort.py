def selectionsort(arr):
    n = len(arr)

    for i in range(n):
        minval = i 
        for j in range(i,n):
            if arr[minval] > arr[j]:
                minval = j
        arr[i],arr[minval] = arr[minval],arr[i]
    return arr 

print(selectionsort([3,2,1]))

## TimeComplexity O(n*2)