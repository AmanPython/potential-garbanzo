import unittest

class Node:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None 

## diameter of the tree
node1 = Node(1)
node1.left = Node(2)
node1.left.left = Node(3)
node1.left.right = Node(4)
node1.left.right.left = Node(5)
node1.left.right.right = Node(6)
node1.right = Node(11)
node1.right.right = Node(12)
node1.right.right.right = Node(13)
node1.right.right.right.right = Node(14)
node1.right.right.left.right = Node(15)
node1.right.right.left.left = Node(16)
