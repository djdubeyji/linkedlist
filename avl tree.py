class node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class avl:
    def insert(self, root, key):
        if not root:
            return ()
