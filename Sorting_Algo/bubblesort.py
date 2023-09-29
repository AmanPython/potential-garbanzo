def bubblesort(arr):
    n = len(arr)
    swapped = True
    for i in range(n):
        if swapped :
            swapped = False
            for j in range(i,n):
                if arr[j] < arr[i]:
                    arr[i],arr[j] = arr[j],arr[i]
                    swapped = True
    return arr 


print(bubblesort([3,2,1]))

## Worst Case Time Complexity : O(n*2)