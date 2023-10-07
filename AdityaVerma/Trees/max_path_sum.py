# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = - 10**9
        def helper_fun(node):
            ## Base condition
            if not node:
                return 0

            ## Hypothesis
            left_height = helper_fun(node.left)
            right_height = helper_fun(node.right)

            curr_max = left_height + right_height + node.val
            self.max_sum = max(curr_max,self.max_sum)

            return node.val + max(left_height,right_height)

        helper_fun(root)
        return self.max_sum