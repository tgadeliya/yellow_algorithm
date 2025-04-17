from .linked_list import LinkedList


class DoublyLinkedListNode:
    def __init__(self, x):
        self.item = x
        self.next = None
        self.prev = None

    def later_node(self, i):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.super().__init__()
        self.tail = None

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def insert_first(self, x):
        new_node = DoublyLinkedListNode(x)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, x):
        new_node = DoublyLinkedListNode(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_first(self):
        if self.head is not None:
            x = self.head.item
            self.head.next.prev = None
            self.head = self.head.next
            return x

    def remove(self, x1, x2):
        L2 = DoublyLinkedList()
        L2.head = x1
        L2.tail = x2
        x1.prev.next = x2.next
        x2.next.prev = x1.prev
        return L2

    def splice(self, x, L2):
        x_next = x.next
        x.next = L2.head
        L2.head.prev = x
        x_next.prev = L2.tail
        L2.tail.next = x_next
        L2.head = None
        L2.tail = None
