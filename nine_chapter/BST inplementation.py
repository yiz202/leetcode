
class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self,val):
        if self.value == val:
            return False
        elif val > self.value:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)
                return True
        elif val < self.value:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
                return True
    def find(self,val):
        if self.value == val:
            return True
        elif val > self.value:
            if self.right:
                self.right.find(val)
            else:
                return False

        elif val < self.value:
            if self.left:
                self.left.find(val)
            else:
                return False







class Tree:
    def __init__(self):
        self.root = Node(None)

    def insert(self,val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)
            return True
    def find(self,val):
        if self.root:
            self.root.find(val)
        else:
            return False



