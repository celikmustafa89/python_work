__author__ = 'Mustafa ÇELİK'


class Deque:
    """ Dequeue is common usage of Stack and Queue in the same data structure.
    Items can be added both beginning and end of dequeue.
    Items can be removed both beginning and end of dequeue.

    Example Usage Scenario: Palindrome Checker is a great example.
    ( bastan ve sondan okunusu ayni olan sozcuklerin tespitinde bu veri yapisi kullanilir.
      Bastan ve sondan bir harf alinarak kiyaslanir.
      Esitlik sona kadar devam ederse palidrom oldugu tespit edilir.)
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":

    d = Deque()
    print("empty: {}".format(d.is_empty()))
    d.add_rear(4)
    print("add_rear(4): {}".format(d))
    d.add_rear('dog')
    print("add_rear(dog): {}".format(d))
    d.add_front('cat')
    print("add_front(cat): {}".format(d))
    d.add_front(True)
    print("add_front(True): {}".format(d))
    print("size: {}".format(d.size()))
    print("empty: {}".format(d.is_empty()))
    d.add_rear(8.4)
    print("add_rear(8.4): {}".format(d))
    print("remove_rear: {}".format(d.remove_rear()))
    print("remove_front: {}".format(d.remove_front()))
    print("dequeue: {}".format(d))
