# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        if not preorder:
            return
        
        root = TreeNode(preorder[0])
        # curr = root
        n = len(preorder)
        
        stack = [root]
        for i in range(1, n):
            
            if preorder[i] < stack[-1].val:
                
                tr = TreeNode(preorder[i])
                stack[-1].left = tr
#                 curr.left = tr
#                 curr = tr
                
                # curr = stack[-1].left
                stack.append(tr)
            elif preorder[i] > stack[-1].val:
                tr = TreeNode(preorder[i])
                popped = TreeNode()
                while stack and stack[-1].val < preorder[i]:
                    popped = stack.pop()
                # print(tr.val)
                # curr.right = tr
                popped.right = tr
                stack.append(tr)
        return root
       