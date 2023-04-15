# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
            
            def dfs(root, num):
                if not root:
                    # if ("".join(arr)) not in res:
                    #     res.add("".join(arr))
                    # # res.append(arr.copy())
                    return 0
                num = num * 10 + (root.val)
                if not root.left and not root.right:
                    return num
                
                
                # print(arr)
                left_dig = dfs(root.left, num)
                
                right_dig = dfs(root.right, num)
                return left_dig + right_dig
                
            return dfs(root, 0)