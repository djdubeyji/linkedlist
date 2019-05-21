class node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        printval = self.head
        while printval is not None:
            print(printval.dataval)
            printval = printval.next

    def atfirst(self, newdata):
        newnode = node(newdata)
        newnode.next = self.head
        self.head = newnode


list = linkedlist()
list.head = node("mon")
e1 = node("tue")
e2 = node("wed")
list.head.next = e1
e1.next = e2
list.atfirst("sun")
list.display()
