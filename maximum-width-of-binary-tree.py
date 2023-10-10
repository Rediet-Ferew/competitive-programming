# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append([root, 0])
        max_width = float('-inf')
        while q:
            n = len(q)
            temp = []
            
            for _ in range(n):
                r, col = q.popleft()
                
                if not r:
                    continue
                    
                q.append([r.left, 2*col])
                q.append([r.right, (2*col) + 1])
                
                temp.append(col)
                
            if temp:
                # print(temp)
                max_width = max(max_width, (temp[-1] - temp[0] + 1))
                
        return max_width