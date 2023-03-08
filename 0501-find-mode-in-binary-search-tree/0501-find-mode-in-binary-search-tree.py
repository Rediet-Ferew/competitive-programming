# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, d):
        if root:
            self.traverse(root.left, d)
            d[root.val] = 1 + d.get(root.val, 0)
            self.traverse(root.right, d)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d_val = {}
        self.traverse(root, d_val)
        d_list = list(d_val.items())
        d_list= sorted(d_list, key = lambda x: x[1])
        res = []
        f = d_list[-1][1]
        res.append(d_list[-1][0])
        d_list.pop()
        while d_list:
            val, freq = d_list.pop()
            if freq != f:
                return res
            else:
                res.append(val)
        return res
            
       