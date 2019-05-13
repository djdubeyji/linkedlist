class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class doubly:
    def __init__(self):
        self.head = None

    def push(self, new):
        new = Node(data=new)
        new.next = self.head
        new.prev = None
        if self.head is not None:
            self.head.prev = new
        self.head = new

    def display(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next


list = doubly()
list.push(6)
list.push(10)
list.display(list.head)
