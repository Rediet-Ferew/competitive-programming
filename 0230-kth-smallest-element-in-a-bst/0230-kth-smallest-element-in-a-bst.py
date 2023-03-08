# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, nodes):
            if root:
                self.traverse(root.left, nodes)
                nodes.append(root.val)
                self.traverse(root.right, nodes)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.traverse(root, ans)
        return ans[k - 1]