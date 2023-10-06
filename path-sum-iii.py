# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        res = []
        visited = set()
        # @cache
        def dfs(node, sum_):
            nonlocal ans
            if not node:
                # res.append(sum_)
                return 
            sum_ += node.val
            if sum_ == targetSum:
                ans += 1
            dfs(node.left, sum_)
            dfs(node.right, sum_)
        def traverse(node):
            if not node:
                return 0
            dfs(node, 0)
            # res.append(ans1)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        # print(res)
        return ans