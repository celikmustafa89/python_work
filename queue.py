__author__ = 'Mustafa ÇELİK'


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":

    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    print("queue: {}".format(q))
    print("dequeue: {}".format(q.dequeue()))
    print("size: {}".format(q.size()))
    q.enqueue("joker")
    print("enqueue: {}".format(q))
    q.clear()
    print("clear: {}".format(q))
