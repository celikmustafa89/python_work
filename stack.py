__author__ = 'Mustafa ÇELİK'


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":

    s = Stack()
    print("is_empty: {}".format(s.is_empty()))
    s.push(4)
    s.push('dog')
    print("last element: {}".format(s.peek()))
    s.push(True)
    print("size: {}".format(s.size()))
    print("is_empty: {}".format(s.is_empty()))
    s.push(8.4)
    print("stack: {}".format(s))
    print("pop: {}".format(s.pop()))
    print("pop: {}".format(s.pop()))
    s.clear()
    print("clear: {}".format(s))

