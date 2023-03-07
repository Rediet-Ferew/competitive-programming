# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(l, r):
            if l == None and r == None:
                return True
            if (not l and r) or (not r and l):
                return False

            val1 = l.val 
            val2 = r.val 

            left_check = symmetric(l.left , r.right)
            right_check = symmetric(l.right, r.left)

            return (left_check and right_check and (val1 == val2))
        if not root or (not root.left and not root.right):
            return True
        else:
            return symmetric(root.left, root.right)