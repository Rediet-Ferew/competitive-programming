class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        self.value = 0
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}
    def searchWord(self, word: str) -> int:
        currN= self.root
        for i in range(len(word)):
            asc = ord(word[i]) - ord('a')
            if not currN.children[asc]:
                return False
            
            currN = currN.children[asc]
        if not currN.isEnd:
            return False
        return True
    def insert(self, key: str, val: int) -> None:
        t = self.searchWord(key)
        val_ = val
        if t:
            val_ -= self.map[key]
        self.map[key] =val
        currNode = self.root
        for i in range(len(key)):
            
            asc = ord(key[i]) - ord('a')
            
            if not currNode.children[asc]:
                node = TrieNode()
                currNode.children[asc] = node

            currNode.children[asc].value += val_
            
            currNode = currNode.children[asc]
        currNode.isEnd = True 

    def sum(self, prefix: str) -> int:
        curr = self.root
        sum_ = 0
        for i in range(len(prefix)):
            asc = ord(prefix[i]) - ord('a')
            if not curr.children[asc]:
                sum_ = 0 
                break
            else:
                sum_ = curr.children[asc].value
            curr = curr.children[asc]
           
        return sum_


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)