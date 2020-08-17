class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.begin = None
            self.end = None
            return node.value
        elif self.end == self.begin.next:
            node = self.end
            self.begin.next = None
            self.end = self.begin
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            last_value = node.next.value
            self.end = node
            self.end.next = None
            return last_value

    def shift(self, obj):
        """Appends a new value at the beginning of the list."""
        node = SingleLinkedListNode(obj, self.begin)
        self.begin = node
        if self.begin.next == None:
            self.end = self.begin

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin == None:
            return None
        else:
            node = self.begin
            self.begin = node.next
            return node.value

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        if self.begin.value == obj:
            self.begin = self.begin.next
            return 0
        else:
            index = 0
            node = self.begin
            node_last = node
            while node:
                if node.value == obj:
                    node_last.next = node.next
                    return index
                node_last = node
                node = node.next
                index += 1

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """Get the value at index."""
        current_index = 0
        node = self.begin
        while node:
            if current_index == index:
                return node.value
            node = node.next
            current_index += 1
        return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        print(mark)
        node = self.begin
        while node:
            print(node)
            node = node.next