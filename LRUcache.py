class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        # self.right.next = self.left
        self.right.prev = self.left
        self.left.next = self.right
        # self.left.next = self.right
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = node.prev = nxt, prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)