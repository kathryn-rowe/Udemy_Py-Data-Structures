class Node(object):

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def __repr__(self):
        return "<Node %s>" % self.data

    def find_DFS(self, data):

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)

    def find_BFS(self, data):

        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree(object):
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return "<Tree root=%s>" % self.root

    def find_in_tree(self, data):
        # Use the Node find method
        return self.root.find_BFS(data)


class BinarySearchNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def find(self, data):

        current = self

        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current.data == current.right
            elif current.data < data:
                current.data = current.left


class BidirectionalNode(object):

    def __init__(self, parent, children=None):
        self.parent = parent
        self.children = children or []
