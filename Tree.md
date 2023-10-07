## Trees
 - [Basic Format](#basic-format) 

### Basic Format
```python
def recursive_fun(node):
    ## Base Condtion of recursion
    if not node:
        return 
    ## Recursive Condtion
    ## Hypothesis
    recursive_fun(node.left)
    recursive_fun(node.right)
    ## Induction Step
    if :
        return
    else :
        return
```
- Initialze the return condtion (base condtion and Induction step) for Small Values
- All the return values should be of same type (int,[],node.pointer)
- Find Height of the Tree
```python
##       Tree Structure
##           1
##          / \
##         2   3
```

```python
def Height(node):
    ## Base Condition of recursion
    if not node:                      ## This will differentiate when left is None and right have value
        return 0                           
    ## Recursive Condition
    ## Hypothesis
    lheight = Height(node.left)
    rheight = Height(node.right)
    ## Induction Step
    return max(lheight+1,rheight+1)
```
