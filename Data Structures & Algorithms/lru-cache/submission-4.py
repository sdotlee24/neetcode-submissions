class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = LinkedList()
        self.lut = {}

    def get(self, key: int) -> int:
        if key not in self.lut:
            return -1
        node = self.lut[key]
        self.cache.dequeNode(node)
        self.cache.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lut:
            node = self.lut[key]
            node.val = value
            self.cache.dequeNode(node)
            self.cache.append(node)
            return
        node = Node(value, key)
        self.lut[key] = node
        self.cache.append(node)
        if len(self.lut) > self.cap:
            removed = self.cache.deque()
            del self.lut[removed.key]


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def dequeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def deque(self):
        node = self.head.next
        self.dequeNode(node)
        return node


class Node:
    def __init__(self, val, key) -> None:
        self.prev = None
        self.next = None
        self.val = val
        self.key = key