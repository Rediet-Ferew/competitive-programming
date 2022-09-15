class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyCount = defaultdict(int) # key: count
        self.cache = defaultdict(OrderedDict) # count : {key: value}
        self.minCount = 0
        
    def updateCount(self, key: int, value: int = None) -> int:
        count = self.keyCount[key]
        
        currentVal = self.cache[count].pop(key)

        if value is not None:
            currentVal = value
            
        self.keyCount[key] += 1
        
        self.cache[count+1][key] = currentVal
        
        if count == self.minCount and not self.cache[count]:
            self.minCount += 1
                
        return currentVal

    def get(self, key: int) -> int:
        if (key in self.keyCount):
            return self.updateCount(key)
            
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        
        if key in self.keyCount:
            self.updateCount(key, value)
            
        else:
            if len(self.keyCount) == self.capacity:
                self.keyCount.pop(self.cache[self.minCount].popitem(last=False)[0])
        
            self.minCount = 1
            self.keyCount[key] = 1
            self.cache[1][key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)