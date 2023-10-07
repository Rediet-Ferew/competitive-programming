class Node:
    def __init__(self):
        self.isTerminal = 0
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        cur = self.root
        for ch in s:
            if not cur.children[ord(ch) - ord('a')]:
                cur.children[ord(ch) - ord('a')] = Node()
            cur = cur.children[ord(ch) - ord('a')]
        cur.isTerminal += 1

    def dfs(self, root, s, idx, pos):
        res = 0
        for i in range(26):
            if root.children[i]:
                newIdx = bisect_right(pos[i], idx)
                if newIdx == len(pos[i]):
                    continue
                res += self.dfs(root.children[i], s, pos[i][newIdx], pos)
        return res + root.isTerminal
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        t = Trie()
        for word in words:
            t.insert(word)
        
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)

        return t.dfs(t.root, s, -1, pos)