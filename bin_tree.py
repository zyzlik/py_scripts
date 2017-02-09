class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value
        self.parent = parent

    def has_left_child(self):
        if self.left:
            return True
        return False

    def has_right_child(self):
        if self.right:
            return True
        return False

    def add_left_child(self, key, value):
        self.left = Node(key=key, value=value)
        self.left.parent = self

    def add_right_child(self, key, value):
        self.right = Node(key=key, value=value)
        self.right.parent = self

    def is_root(self):
        if not self.parent:
            return True
        return False

    def is_leaf(self):
        if not self.left and not self.right and self.parent:
            return True
        return False

    def is_left_child(self):
        if self.parent.left == self:
            return True
        return False

    def is_right_child(self):
        if self.parent.right == self:
            return True
        return False

    def has_child(self):
        if self.has_left_child() or self.has_right_child():
            return True
        return False

    def has_only_one_child(self):
        if self.left and not self.right:
            return True
        elif self.right and not self.left:
            return True
        return False

    def add(self, key, value):
        if self.key > key:
            if self.has_left_child():
                self.left.add(key, value)
            else:
                self.add_left_child(key, value)
        elif self.key < key:
            if self.has_right_child():
                self.right.add(key, value)
            else:
                self.add_right_child(key, value)
        elif self.key == key:
            self.value = value

    def display(self):
        print self
        if self.has_child():
            if self.has_left_child():
                self.left.display()
            if self.has_right_child():
                self.right.display()
        else:
            return self

    def search(self, key):
        if self.key == key:
            return self
        if self.key > key and self.has_left_child():
            print 'go to left'
            return self.left.search(key)
        elif self.key < key and self.has_right_child():
            print 'go to right'
            return self.right.search(key)
        return 'Not found'

    def __str__(self):
        return str((self.key, self.value))

    def __repr__(self):
        return str(self.key)


class BSTree:
    def __init__(self, key, value):
        self.root = Node(key=key, value=value)

    def add(self, key, value):
        return self.root.add(key, value)

    def search(self, key):
        return self.root.search(key)

    def remove(self, key):
        node = self.search(key)
        if node:
            print 'We have to remove %s' % (node)
        else:
            return 'No such key'
        if node.is_leaf():
            if node.is_left_child():
                node.parent.left = None
            if node.is_right_child():
                node.parent.right = None

        elif node.has_only_one_child():
            if node.has_left_child():
                if node.is_left_child():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.is_right_child():
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    self.root = node.left
            elif node.has_right_child():
                node.right.parent = node.parent
                if node.is_left_child():
                    node.parent.left = node.right
                if node.is_right_child():
                    node.parent.right = node.right
                else:
                    self.root = node.right
        else:
            print 'node has two child'
            if node.right.left:
                successor = node.right.left
                while successor.has_left_child():
                    successor = successor.left
                # node.key = successor.key
                # node.value = successor.value
                if successor.has_right_child():
                    successor.right.parent = successor.parent
                    successor.parent.right = successor.right
                else:
                    successor.parent.left = None
                successor.left = node.left
                node.left.parent = successor
                successor.right = node.right
                node.right.parent = successor
                successor.parent = node.parent
                if not successor.parent:
                    self.root = successor
            else:
                successor = node.right
                successor.left = node.left
                successor.parent = node.parent
                node.left.parent = successor
                if node.is_left_child():
                    node.parent.left = successor
                else:
                    node.parent.right = successor
        return self

    def __str__(self):
        return self.root.display()

tree = BSTree(10, 'a')
tree.add(5, 'b')
tree.add(15, 'c')
tree.add(7, 'd')
tree.add(17, 'e')
tree.add(17, 'r')
tree.add(13, 'g')
tree.add(14, 'g')
tree.add(3, 'f')
tree.remove(14)
tree.root.display()
tree.search(13)
tree.root.display()
