# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_parent_key(self, root, key):
            if not root:
                return None
            if root.right and root.right.val == key:
                return root
            elif root.left and root.left.val == key:
                return root
            if key > root.val:
                return self.get_parent_key(root.right, key)
            elif key < root.val:
                return self.get_parent_key(root.left, key)
    def inorder_successor(self, root):
        if not root.left:
            return root
        return self.inorder_successor(root.left)
        # self.inorder_successor(root.right, node)
            
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        d = self.get_parent_key(root, key)
        if root.val != key and d == None:
            return root
        
        deleted_node = TreeNode()
        if root.val == key:
            deleted_node = root
            
        else:
            if d.left and d.left.val == key:
                deleted_node = d.left 
            elif d.right and d.right.val == key:
                deleted_node = d.right
        
         
        #has 'deleted' no child, leaf node
        if not deleted_node.left and not deleted_node.right:
            if deleted_node == root:
                return None
            if d.left and d.left.val == key:
                d.left = None
            elif d.right and d.right.val == key:
                d.right = None
            return root
            
        # #has only one child
        if not deleted_node.right and deleted_node.left:
            if deleted_node == root:
                root = root.left
            else:
                parent = self.get_parent_key(root, deleted_node.val)
                if parent.left and parent.left.val == key:

                    parent.left = deleted_node.left
                elif parent.right and parent.right.val == key:
                    parent.right = deleted_node.left
            # node = deleted_node.left
            # deleted_node.val = node.val
            # deleted_node.left = None
            return root
        if not deleted_node.left and deleted_node.right:
            if deleted_node == root:
                root = root.right
            else:
                parent = self.get_parent_key(root, deleted_node.val)
                if parent.left and parent.left.val == key:
                    parent.left = deleted_node.right
                elif parent.right and parent.right.val == key:
                    parent.right = deleted_node.right
            # node = deleted_node.right
            # deleted_node.val = node.val
            # deleted_node.right = None
            return root
        min_val = self.inorder_successor(deleted_node.right)
        #has two children
        
        parent_min = self.get_parent_key(root, min_val.val)
    
        deleted_node.val, min_val.val = min_val.val, deleted_node.val
        
        if parent_min.left and parent_min.left.val == key:
            
            if min_val.right:
                parent_min.left = min_val.right
            else:
                parent_min.left = None
        elif parent_min.right and parent_min.right.val:
            if min_val.right:
                parent_min.right = min_val.right
            else:
                parent_min.right = None
    
        return root
        