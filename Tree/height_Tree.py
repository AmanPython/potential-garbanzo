def height(node):
   if not node:
      return 0
   lheight = height(node.left)
   rheight = height(node.right)
   ## Recursion Function
   if lheight > rheight:
      return 1 + lheight
   else:
      return 1 + rheight