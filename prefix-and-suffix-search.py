class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end =  False
        self.index = []
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words

        self.prefixTrie = TrieNode()
        self.suffixTrie = TrieNode()

        # print(self.words[6413])
        for idx, word in enumerate(self.words):
            # print(word)
            currNode_1 = self.prefixTrie
            for i in range(len(word)):
                asc = ord(word[i]) - ord('a')
                if not currNode_1.children[asc]:
                    node = TrieNode()
                    currNode_1.children[asc] = node
                currNode_1.children[asc].index.append(idx)
                currNode_1 = currNode_1.children[asc]
            currNode_1.isEnd = True
        
        for idx, word in enumerate(self.words):
            # print(word)
            currNode_2 = self.suffixTrie
            for i in range(len(word) - 1, -1, -1):
                asc = ord(word[i]) - ord('a')
                if not currNode_2.children[asc]:
                    node = TrieNode()
                    # node.index.append(idx)
                    currNode_2.children[asc] = node
               
                currNode_2.children[asc].index.append(idx)
                currNode_2 = currNode_2.children[asc]
            currNode_2.isEnd = True
    def f(self, pref: str, suff: str) -> int:
        
        currNode_1 = self.prefixTrie
        currNode_2 = self.suffixTrie
        
        for i in range(len(pref)):
            asc = ord(pref[i]) - ord('a')

            if not currNode_1.children[asc]:
                return -1
            currNode_1 = currNode_1.children[asc]
        for i in range(len(suff) - 1, -1, -1):
            asc = ord(suff[i]) - ord('a')
            if not currNode_2.children[asc]:
                return -1
            currNode_2 = currNode_2.children[asc]
        list_1 = currNode_1.index
        list_2 = currNode_2.index
        # print(list_1)
        # print(list_2)
        end_1 = len(list_1) - 1
        end_2 = len(list_2) - 1
        
        while end_1 >= 0 and end_2 >= 0:
            if list_1[end_1] == list_2[end_2]:
            
                return list_1[end_1]
            elif list_1[end_1] > list_2[end_2]:
                end_1 -= 1
            else:
                end_2 -= 1
            
        return -1
            



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)