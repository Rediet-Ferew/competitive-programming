class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()
        pair = ""
        for j in range(len(words)):
            word = words[j]
            currNode = self.root
            flag = False
            for i in range(len(word)):
                asc = ord(word[i]) - ord('a')
                
                if not currNode.children[asc] and i != len(word) - 1:
                    break
                elif not currNode.children[asc] and i == len(word) - 1:
                    flag = True
                    node = TrieNode()
                    currNode.children[asc] = node
                    if len(word) > len(pair):
                        pair = word
                
                currNode = currNode.children[asc]
            if flag:
                currNode.isEnd = True
        return pair