# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if (not p and q) or (not q and p):
            return False
        
        val1 = p.val 
        val2 = q.val 
        
        left_check = self.isSameTree(p.left , q.left)
        right_check = self.isSameTree(p.right, q.right)
        
        return (left_check and right_check and (val1 == val2))
        
        
        