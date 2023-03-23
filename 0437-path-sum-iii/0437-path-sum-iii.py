# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkSum(self,root, target):
        if not root:
            return 
        if root.val == target:
            self.paths += 1
        self.checkSum(root.left, target - root.val)
        self.checkSum(root.right, target - root.val)
    def traverse(self,root, target):
        if not root:
            return
        self.checkSum(root, target)
        self.traverse(root.left, target)
        self.traverse(root.right, target)
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        self.paths = 0
        self.traverse(root, target)
        return self.paths