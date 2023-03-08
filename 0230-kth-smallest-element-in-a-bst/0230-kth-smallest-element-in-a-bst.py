# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_successor(self, root, stk):

        if not root:
            return None
        stk.append(root)
    
        return self.inorder_successor(root.left, stk)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ans = []
        # self.traverse(root, ans)
        # return ans[k - 1]
        level = 0
        stack = []
        r = root
        
        while stack or r:
            while r:
                stack.append(r)
                r = r.left
            
            r = stack.pop()
            level += 1
            if level == k:
                return r.val
            r = r.right
        
        
            
        
