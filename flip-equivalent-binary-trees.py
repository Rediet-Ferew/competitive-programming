# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        st1 = set()
        st2 = set()

        def dfs1(parent, root1):
            if not root1:
                return None
            dfs1(root1, root1.left)
            dfs1(root1, root1.right)
            if parent != -1:
                st1.add((parent.val, root1.val))
            else:
                st1.add((-1, root1.val))
        def dfs2(parent, root2):
            if not root2:
                return None
            dfs2(root2, root2.right)
            dfs2(root2, root2.left)
            if parent != -1:
                st2.add((parent.val, root2.val))
            else:
                st2.add((-1, root2.val))
        dfs1(-1, root1)
        # print("*******")
        dfs2(-1, root2)
        st = st1.intersection(st2)
        if len(st) == len(st1) == len(st2):
            return True
        return False