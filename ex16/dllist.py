class DoubleLinkedListNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        if self.end:
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node
        else:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin

    def pop(self):
        """Removes the last item and returns it."""
        if self.end:
            node = self.end
            if self.end == self.begin:
                self.begin = None
                self.end = None
            else:
                self.end = node.prev
                self.end.next = None
                if self.end == self.begin:
                    self.begin.next = None
            return node.value
        else:
            return None

    def shift(self, obj):
        """Actually just another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin:
            node = self.begin
            if self.begin == self.end:
                self.begin = None
                self.end = None
            else:
                self.begin = node.next
                self.begin.prev = None
            return node.value
        else:
            return None

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove(). It should take a node, and detach it from the
        list, whether the node is at the front, end, or in the middle."""
        if node == self.begin:
            self.unshift()
        elif node == self.end:
            self.pop()
        else:
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node_next
            node_next.prev = node_prev

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        index = 0
        while node:
            if node.value == obj:
                self.detach_node(node)
                return index
            index += 1
            node = node.next
        return -1

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        count = 0
        node = self.begin
        while node:
            count += 1
            node = node.next
        return count        

    def get(self, index):
        """Get the value at index."""
        node = self.begin
        current_index = 0
        while node:
            if current_index == index:
                return node.value
            current_index += 1
            node = node.next
        return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        print(mark)
        while node:
            print(node)
            node = node.next

    def _invariant(self):
        if self.begin == None:
            assert self.end == None, "End set while begin is not."

        if self.begin:
            assert self.begin.prev == None, "begin.prev not None"
            assert self.end.next == None, "end.next not None"
