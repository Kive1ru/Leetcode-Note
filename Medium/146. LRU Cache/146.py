class doubleList:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = doubleList()
        self.tail = doubleList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            self.moveToHead(key)
            res = self.cache[key].value
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.moveToHead(key)
        else:
            if len(self.cache) >= self.capacity:
                self.removeTail()
            self.addToHead(key, value)

    def moveToHead(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def addToHead(self, key, value):
        new = doubleList(key, value)
        self.cache[key] = new
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new
    
    def removeTail(self):
        last = self.tail.prev
        self.cache.pop(last.key)
        last.prev.next = self.tail
        self.tail.prev = last.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)