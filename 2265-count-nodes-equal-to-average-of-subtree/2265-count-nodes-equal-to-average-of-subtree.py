# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_sum(self, root, sum_, n):
        if root:
            
            self.get_sum(root.left, sum_ , n)
            sum_[-1] += root.val
            n[-1] += 1
            self.get_sum(root.right, sum_, n)
            
        return (sum_, n)
            
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        stack = [root]
        avrgs = 0
        
        while stack:
            r = stack.pop()
            if not r:
                continue
            summ, num = self.get_sum(r, [0], [0])
            
            avrg = summ[0] // num[0]
            
            if r.val == avrg:
                avrgs += 1
                
            stack.append(r.left)
            stack.append(r.right)
        return avrgs