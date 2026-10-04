class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = LinkedList()
        self.lut = {}
        self.size = 0
    def get(self, key: int) -> int:
        if key not in self.lut:
            return -1
        node = self.lut[key]
        self.cache.dequeNode(node)
        self.cache.append(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        node = Node(value, key)
        if key in self.lut:
            node = self.lut[key]
            self.cache.dequeNode(node)
            node.val = value
            self.cache.append(node)
            return
        self.lut[key] = node
        self.cache.append(node)
        if self.size == self.cap:
            removed = self.cache.deque()
            del self.lut[removed.key]
            self.size -= 1
        
        self.size += 1

class LinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
    def append(self, node):
        tail = self.tail.prev
        tail.next = node
        node.prev = tail
        node.next = self.tail
        self.tail.prev = node
    def dequeNode(self, node):
        prev = node.prev
        node.prev.next = node.next
        node.next.prev = prev
    def deque(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        return node

class Node:
    def __init__(self, val, key) -> None:
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
        