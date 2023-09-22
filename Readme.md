## Strive CheatSheet
 - Day 7
    - [Rotate a linked list](#rotate-a-linked-list)
 - Day 9
    - 

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
 - Logical Issues 
    - Did not break recursion using return
    - Duplicates elements in array, I have sorted the array, and same array had to pop an element, the poped element became different after sorting.
    - Deep Copy and Shallow copy
    ```python
    arr = [1,2,4,5]
    val = arr          # shallow copy
    val2 = arr[:]      # deep copy
    ```
 - Naming Convention Issues
   | S.No. | Aman | ChatGPT | Striver |
   |--- | ---| ---- | ---- |
   | 1. | start/node | current | temp |
   | 2. | n/count | length | length |
   | 3. | target/end | No Name | end |
   | 4. | nex   | new_head | head |