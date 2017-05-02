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