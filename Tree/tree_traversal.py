from collections import deque

## Node Initialization
class Node():
    def __init__(self,val):             ## Tree Initialization 
        self.val = val 
        self.left = None 
        self.right = None 

## Case -1 
head = Node(1)                          ##         1
head.left = Node(2)                     ##        / \
head.right = Node(3)                    ##       2   3
head.left.left = Node(4)                ##      / \ / \
head.left.right = Node(5)               ##     4  5 6  7
head.right.left = Node(6)               ##
head.right.right = Node(7)              ##

def postorder(node):                ## 4->5->2->6->7->3->1
    """
    :type node: Node
    """
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

def postorder_iterative(root):
    """
    :type node: Node
    :rtype arr: List
    """
    if not root:
        return []

    result = []
    stack = []
    prev_node = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack[-1]

        # Check if the right subtree is visited or not, or if it doesn't exist.
        if not root.right or root.right == prev_node:
            result.append(root.val)
            stack.pop()
            prev_node = root
            root = None
        else:
            root = root.right

    return result


def inorder(node):                  ## 4->2->5->1->6->3->7
    """
    :type node: Node
    """
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def inorder_iterative(root):
    if not root:
        return []

    result = []
    stack = []

    while root or stack:
        # Traverse to the leftmost node
        while root:
            stack.append(root)
            root = root.left

        # Pop the top node from the stack
        root = stack.pop()
        result.append(root.val)

        # Move to the right subtree
        root = root.right

    return result

def preorder(node):                 ##  1->2->4->5->3->6->7
    """
    :type node: Node
    """
    if node:                            
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def preorder_iterative(node):       ## [1, 2, 4, 5, 3, 6, 7]
    """
    :type node: Node
    :rtype :    arr
    """
    # Use Queue
    queue = deque()
    queue.appendleft(node)
    sol = []
    while queue:
        head = queue.popleft()
        sol.append(head.val)
        if head.right:
            queue.appendleft(head.right)
        if head.left:
            queue.appendleft(head.left)
    return sol 


## Create Tree From level order traversal
def createTreeFromArray(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None

    root = Node(arr[index])
    root.left = createTreeFromArray(arr, 2 * index + 1)
    root.right = createTreeFromArray(arr, 2 * index + 2)

    return root

root2 = createTreeFromArray([1,2,3,4,5,6,7])

if __name__ == '__main__':
    print("Pre-order traversal",preorder(root2))
    print(preorder_iterative(root2))
    print("Post-order traversal",postorder(root2))
    print(postorder_iterative(root2))
    print("In-order traversal",inorder(root2))
    print(inorder_iterative(root2))
