# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        @cache
        def dfs(p, node, sum_, arr):
            
            if not node and not p.left and not p.right:
                if sum_ == targetSum:
                    ans.append(arr)
                return 
            if not node:
                return
            dfs(node, node.right, sum_ + node.val, arr + (node.val, ))
            dfs(node, node.left, sum_ + node.val, arr + (node.val, ))
            # arr.pop()
        
        # print(ans)
        if not root:
            return []
        dfs(-1, root, 0, ())
        # ans = list(ans)
        temp = []
        for t in range(len(ans)):
            a = list(ans[t])
            # print(a)
            if a:
                temp.append(a)

        return temp