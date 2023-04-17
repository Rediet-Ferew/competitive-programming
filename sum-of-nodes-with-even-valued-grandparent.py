# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(root, parent, grandpa):

            if not root:
                return 0
            
            
            total = 0
            if grandpa % 2 == 0:
                total = root.val
            total += dfs(root.left, root.val, parent)
            
            total += dfs(root.right, root.val, parent)
            
            return total
            
        return dfs(root, 1, 1)