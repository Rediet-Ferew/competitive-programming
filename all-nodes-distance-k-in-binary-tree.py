# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj_list = defaultdict(list)
        def traverse(root):
            if not root:
                return 
            if root.left:
                adj_list[root.left.val].append(root.val)
                adj_list[root.val].append(root.left.val)
            if root.right:
                adj_list[root.right.val].append(root.val)
                adj_list[root.val].append(root.right.val)
            traverse(root.left)
            traverse(root.right)
            
        if k == 0:
            return [target.val]
        traverse(root)
        visited = set()
        visited.add(target.val)
        q = collections.deque()
        q.append(target.val)
        
        level = 0
        ans = []
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                val = q.popleft()
                for item in adj_list[val]:
                    if item != target.val and level + 1 == k and item not in visited:
                        ans.append(item)
                        
                    if item not in visited:
                        q.append(item)
                        visited.add(item)
            level += 1
        return ans