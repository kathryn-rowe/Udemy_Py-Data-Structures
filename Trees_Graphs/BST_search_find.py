# Build a binary search tree

class TreeNode(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def find(self, sought):

        current = self

        while current:
            if current.data == sought:
                return current
            elif current.data < sought:
                current = current.left
            elif current.data > sought:
                current = current.right

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isleftChild(self):
        return self == self.parent.left and self.parent

    def isrightChild(self):
        return self == self.parent.right and self.parent

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self, data, lc, rc):
        self.data = data
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def insert(self, data):

        new_node = TreeNode(data)

        if self.root:
            self._insert(data)
        else:
            self.root = new_node
        self.size += 1

    def _insert(self, data):

        new_node = TreeNode(data)

        if data <= self.data:
            if not self.left:
                self.left == new_node
            else:
                self.left._insert(data)

        elif data > self.data:
            if not self.right:
                self.right == new_node
            else:
                self.right._insert(data)

        return self
