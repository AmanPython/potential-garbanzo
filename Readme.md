## Strive CheatSheet
 - Day 7
    - [Rotate a linked list](#rotate-a-linked-list)
    - 
 - Day 9
    - 
 - Day 17
    - [Bottom view of binary Tree](#bottom-view-of-binary-tree)
    - [Maximum width of binary Tree](#maximum-width-of-binary-tree)
    - [Height of Binary Tree](#height-of-binary-tree)

 ## Bottom View of Binary Tree
 - Pre-Order Traversal
 - Hash table with tuples
 - Maintaining Horizontal distance at every level from the node
 - Last updated tuples will be the answer, update the hashtable based on greater level
 ```python
    bottom_view_map = {}
    # Update the bottom view for the current horizontal distance
    bottom_view_map[horizontal_distance] = (node.val, level)
    sorted_bottom_view = sorted(bottom_view_map.items())  ## this will sort based on the keys
   
    # Getting the sorted elements
    for _, (key, _) in sorted_bottom_view:
    print(key, end=" ")
 ```
 ## Maximum Width of Binary Tree
 - 
 
## Height of Binary Tree
 - Post-Order Traversal



## LinkedList Observations:
 - Updating linked list
    ```python
     newhead = Node(5)           ## updating the reference value
     newhead.next = Node(1)      ## Updating reference of the pointer 
     newhead.val = 8             ## Updating the value at node
    ```
 - Use of while loop for iteration
    - Way 1:
        ```python
        length = 1
        while current.next:
            current = current.next
            length += 1
        ```
        - At the end, this will point to the last node, can use last node here
    - Way 2:
        ```python
        length = 0
        while current:
            current = current.next
            length += 1
        ```
        - At the end, this will point to None, can't use last node from here


### Rotate a Linked List
 #### WhitePaper Solution 
 - Logical Issues
    - Did not consider the base case, when length is zero, one or k is zero
    - Breaking when k is zero (did not consider this case)
    - Could have updated the end point on first Iteration (striver approch).
    - Iteration Problem, if k == 0: return head, before this, I made the linked list as a cycle. This returned a cycle.
 - Naming Convention Issues
   | S.No. | Aman | ChatGPT | Striver |
   |--- | ---| ---- | ---- |
   | 1. | start/node | current | temp |
   | 2. | n/count | length | length |
   | 3. | target/end | No Name | end |
   | 4. | nex   | new_head | head |

#### Time and Space Complexity
 - Time : O(N) or O(N + k), where N is the number of nodes
 - Space : O(1)


 ## Recursion Observation
 #### WhitePaper Solution 
 - subsetSums
 - Logical Issues 
    - Did not break recursion using return
    - Duplicates elements in array, I have sorted the array, and same array had to pop an element, the poped element became different after sorting.
    - Deep Copy and Shallow copy
    ```python
    arr = [1,2,4,5]
    val = arr          # shallow copy
    val2 = arr[:]      # deep copy
    ```
 - Naming Convention Issues (subsetSums)
   | S.No. | Aman | ChatGPT | Striver |
   |--- | ---| ---- | ---- |
   | 1. | all_sol | all_sum | ans |
   | 2. | helper_fun | generate_subset_sums | subsetSumsHelper |
   | 3. | total_sum | current_sum | sum |
   | 4. | n | index | ind |

 - allsubsets
 - Logical Issues
   - Duplicates Removal Solution

 - Naming Convention Issues (allsubsets)
   | S.No. | Aman | ChatGPT | Striver |
   |--- | ---| ---- | ---- |
   | 1. | all_sol | all_subsets |  |
   | 2. | helper_fun | generate_subsets | |
   | 3. | arr | current_subsets | |
   | 4. | n | index |  |
 
 - Their is issue, where to use _ and where not to use.