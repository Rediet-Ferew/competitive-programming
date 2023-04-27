# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque()
        if not root:
            return []
        q.append(root)
        

        while q:
            cur_len = len(q)
            temp = 0
            for _ in range(cur_len):
                curr = q.popleft()
                
                temp += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
           
            ans.append(temp/cur_len)
        return ans