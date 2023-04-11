"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(root, cnt):
            
            if not root:
                return cnt
            max_dep = cnt
            
        
            for node in root.children:
                dep = dfs(node, cnt + 1)
                
                max_dep = max(max_dep, dep)
            return max_dep
                
        return dfs(root, 1)