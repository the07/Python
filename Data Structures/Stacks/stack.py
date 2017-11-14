class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        """change this to self.items.insert(0, item)"""
        self.items.append(item)

    def pop(self):
        """/* change this to self.items.pop(0) */"""
        if len(self.items) == 0:
            return "Stack already empty"
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
