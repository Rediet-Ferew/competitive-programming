# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insertion(root, val):
            if not root:
                return None
            
            if not root.right and val > root.val:
                root.right = TreeNode(val)

            elif not root.left and val < root.val:
                root.left = TreeNode(val)
                 
            if val > root.val:
                return self.insertIntoBST(root.right, val)

            elif val < root.val:
                return self.insertIntoBST(root.left, val)
        root_returned = root
        if not root_returned:
            root = TreeNode(val)
            return root
        insertion(root_returned, val)
        return root