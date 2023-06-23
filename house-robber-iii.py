# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dp(root):
            # nonlocal max_val
            if not root:
                return 0
            if root in memo:
                return memo[root]
            max_val = 0
            if root.left:
                max_val += dp(root.left.left) + dp(root.left.right)
            if root.right:
                max_val += dp(root.right.left) + dp(root.right.right)

            #either from itself or from its children
            max_val = max(max_val + root.val, dp(root.left) + dp(root.right))
            memo[root] = max_val
            return max_val
        
        return dp(root)