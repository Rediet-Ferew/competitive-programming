# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(root, ans):
            
            
            if root:
                
                traverse(root.left, ans)
                ans.append(root.val)
                
                traverse(root.right, ans)
        
        ans = []
        traverse(root, ans)
        return ans