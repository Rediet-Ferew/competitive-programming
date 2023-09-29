class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str, l: int, bin_len: int) -> None:
        word = "0" * ((l + 1) - bin_len) + word
        currNode = self.root
        for i in range(len(word)):
            
            asc = int(word[i])
            
            if not currNode.children[asc]:
                node = TrieNode()
                
                currNode.children[asc] = node
            currNode = currNode.children[asc]
        currNode.isEnd = True 

    
    def search(self, word: str, l: int, bin_len: int) -> bool:
        max_num = ""
        word = ("0" * ((l + 1) - bin_len)) + word
        currNode = self.root
        currN = self.root
        for i in range(len(word)):
            asc = int(word[i])
            if asc == 0:
                currNode = currNode.children[asc]
                
                if currN.children[1] != None:
                    currN = currN.children[1]
                    max_num += "1"
                elif currN.children[0] != None:
                    currN = currN.children[0]
                    max_num += "0"
                else:
                    max_num += "0"
                    break
                    
            else:
                currNode = currNode.children[asc]
                
                if currN.children[0] != None:
                    currN = currN.children[0]
                    max_num += "1"
                elif currN.children[1] != None:
                    currN = currN.children[1]
                    max_num += "0"
                else:
                    max_num += "0"
                    break
                    
        return max_num
class Solution:
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        l = len(bin(max(nums))) - 2
        max_xor = 0
        mask = 0
        for i in range(30, -1, -1):
            mask |= 1 << i
            curr_xor = max_xor | (1 << i)
            prefix = set()

            for num in nums:
                prefix.add(num & mask)
            for p in prefix:
                if curr_xor ^ p in prefix:
                    max_xor = curr_xor
                    break
        
        return max_xor