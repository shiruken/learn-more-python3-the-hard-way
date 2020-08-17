class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class Queue(object):
    
    def __init__(self):
        self.head = None
        self.tail = None

    def shift(self, obj):
        """Appends a new value on the end of the queue."""
        if self.tail:
            node = QueueNode(obj, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.head = QueueNode(obj, None, None)
            self.tail = self.head

    def unshift(self):
        """Removes the first item and returns it."""
        if self.head:
            node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = node.next
                self.head.prev = None
            return node.value
        else:
            return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""        
        return self.head.value

    def count(self):
        """Counts the number of elements in the queue."""
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count        

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the queue."""
        node = self.head
        print(mark)
        while node:
            print(node)
            node = node.next
