# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = [p]
        q_list = [q]
        p_ = p.val
        q_ = q.val
        def dfs(parent, node):
            nonlocal p_
            nonlocal q_
            if not node:
                return 
            dfs(node, node.right)
            dfs(node, node.left)
            v = node.val
            # print(parent, node)
            if v == p_ and parent != -1:
                p_list.append(parent)
                
                if parent != -1:
                    p_ = parent.val
            if v == q_ and parent != -1:
                q_list.append(parent)
                
                if parent != -1:
                    q_ = parent.val
            
        dfs(-1, root)
        
        r1 = len(p_list) - 1
        r2 = len(q_list) - 1
        ans = -1
        while r1 >= 0 and r2 >= 0:
            # print(p_list[r1].val,  q_list[r2].val)
            if p_list[r1].val == q_list[r2].val:
                ans = p_list[r1]
                r1 -= 1
                r2 -= 1
            else:
                break
            
            
        return ans