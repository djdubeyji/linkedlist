class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class header:
    def __init__(self):
        self.head = None
    def display(self):
        dis = self.head
        while dis is not None:
            print(dis.data)
            dis=dis.next
    def insertatfirst(self,new):
        newnode = node(new)
        newnode.next=self.head
        self.head=newnode
    def insertatend(self, newdata1):
        newnode1 =node(newdata1)
        if self.head is None:
            self.head -newnode1
            return
        last = self.head
        while(last.next):
            last=last.next
        last.next=newnode1
list1 = header()
list1.head= node("mon")
n1 = node("tue")
n2 = node("wed")
list1.head.next =n1
n1.next=n2
list1.display()
list1.insertatfirst("sun")
list1.display()
list1.insertatend("thu")
list1.display()