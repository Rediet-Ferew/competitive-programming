# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # arr = []
        def dfs(root):
            
            
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val)
          
            value = str(root.val)
            v = ""
            v += value
            left = dfs(root.left)
            right = dfs(root.right)
            v += ('(' + str(left) + ')')
            v += ('(' + str(right) + ')')
            # arr.append(v)
            return v
        arr = list(dfs(root))
        n = len(arr)
        for i in range(0, n - 1):
            if arr[i] == '(' and arr[i + 1] == ')':
                if ((i + 2 < n) and arr[i + 2] == ')') or (i + 2 == n):
                    arr[i] = ""
                    arr[i + 1] = ""
                
        return "".join(arr)