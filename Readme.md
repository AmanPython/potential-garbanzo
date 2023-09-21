## Strive CheatSheet
 - Day 7
    - [Rotate a linked list](#rotate-a-linked-list)

## LinkedList Observations:
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