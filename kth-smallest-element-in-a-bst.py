# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = []
        def dfs(root):
            nonlocal cnt
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        dfs(root)
        ans.sort()
        return ans[k - 1]