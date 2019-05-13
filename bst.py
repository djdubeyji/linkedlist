class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + "not found"
            return self.left.search(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + "not found"
            return self.right.search(val)
        else:
            print(str(self.data) + "is found")


root = node(10)
root.printtree()
root.insert(6)
root.insert(14)
root.insert(3)
root.printtree()
print(root.search(8))
print(root.search(14))
