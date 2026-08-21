class ListNode():
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.count = 0
    
    def addNode(self, node: ListNode):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node
    
    def removeNode(self, node: ListNode):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.count += 1
        
        self.addNode(node)
        

        if self.count > self.capacity:
            del self.cache[self.head.next.key]
            self.removeNode(self.head.next)
            self.count -= 1

        