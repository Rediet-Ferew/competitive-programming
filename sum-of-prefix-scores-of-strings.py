class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        currNode = self.root
        for i in range(len(word)):
            asc = ord(word[i]) - ord('a')
            if not currNode.children[asc]:
                node = TrieNode()
                currNode.children[asc] = node
            currNode.children[asc].count += 1
            currNode = currNode.children[asc]
        currNode.isEnd = True
    def search(self, word: str):
        cnt = 0
        currNode = self.root
        for i in range(len(word)):
            asc = ord(word[i]) - ord('a')
            cnt += currNode.children[asc].count
            currNode = currNode.children[asc]
        return cnt
class Solution:
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            t = trie.search(word)
            ans.append(t)
        # print(ans)
        return ans