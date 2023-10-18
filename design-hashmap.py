class MyHashMap:

    def __init__(self):
        self.hashTable = [None for i in range(1000001)]
        
    def put(self, key: int, value: int) -> None:
        if self.hashTable[key] != None:
            self.hashTable[key][1] = value
        else:
            self.hashTable[key] = [key, value] 

    def get(self, key: int) -> int:
        if not self.hashTable[key]:
            return -1
        else:
            return self.hashTable[key][1]

    def remove(self, key: int) -> None:
        self.hashTable[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)