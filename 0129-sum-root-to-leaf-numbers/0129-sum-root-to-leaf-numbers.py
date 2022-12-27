# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def getDigit(curr, digit):
            if not curr:
                return 0
            
            digit = digit * 10 + curr.val
            
            if not curr.left and not curr.right:
                return digit
            return getDigit(curr.left, digit) + getDigit(curr.right, digit)
        return getDigit(root, 0)
        