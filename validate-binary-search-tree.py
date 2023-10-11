# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upper = float('inf') #right min
        lower = float('-inf') #left_max
        return self.validate(root, lower, upper)
    def validate(self,root, lower, upper):
        if root == None:
            return True

        if root.val >= upper or root.val <= lower:
            return False

        return self.validate(root.left, lower, root.val) and self.validate(root.right, root.val, upper)
    
    
    
    
#         def traverse(root, ans):
            
            
#             if root:
                
#                 traverse(root.left, ans)
                
#                 ans.append(root.val)
                
#                 traverse(root.right, ans)
        
#         ans = []
#         traverse(root, ans)
#         return ans == sorted(set(ans))