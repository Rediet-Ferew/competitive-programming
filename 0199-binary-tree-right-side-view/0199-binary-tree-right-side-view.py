# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_right(self, root, nodes):
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            temp = []
            # r = TreeNode()
            for _ in range(n):
                r = q.popleft()
                
                if not r:
                    continue
        
                q.append(r.left)
                q.append(r.right)
                
                temp.append(r.val)
                
            if temp:
                nodes.append(temp[-1])
                
        return nodes
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traverse_right(root, ans)
        return ans