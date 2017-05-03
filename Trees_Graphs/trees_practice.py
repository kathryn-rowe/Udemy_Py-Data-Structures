# Tree Node represented as a Class
class Node(object):

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data


class BinaryTree(object):

    def __init__(self, root):

        self.data = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):

        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.data = obj

    def getRootVal(self):
        return self.data

    def _add(self, data):

        new_node = Node(data)

        if not self.item:
            self.item = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left._add(data)

        return self

    def _search(self, value):

        if self.data == value:
            return True

        found = False

        if self.left:
            found = self.left._search(value)
        if self.right:
            found = found or self.right._search(value)
        return found
