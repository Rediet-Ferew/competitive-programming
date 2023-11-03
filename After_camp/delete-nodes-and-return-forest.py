# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        parents = {}
        def dfs(root, parent,left):
            if not root:
                return
            
            if root.val in to_delete:
                p = parent
                l = left
                dfs(root.left, -1, True)
                dfs(root.right, -1, False)
                if l and p != -1:
                    p.left = None
                elif (not l) and p != -1:
                    p.right = None
            else:
                dfs(root.left, root, True)
                dfs(root.right, root, False)
            parents[root] = parent
        
    
        dfs(root, -1, True)
        
        for k, v in parents.items():
            if v == -1 and k.val not in to_delete:
                ans.append(k)
                # print(k.val)
        return ans

            
            
