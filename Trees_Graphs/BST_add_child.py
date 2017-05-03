class Node(object):
    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here.
        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(7, Node(5), Node(8))
        ... )
        >>> t.insert(0)
        >>> t.left.left.left.data == 0
        True
        >>> t.left.left.right is None
        True
        """

        new_node = Node(new_data)

        if not self.data:
            self.data = new_node
        else:
            if new_data < self.data:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(new_data)
            elif new_data > self.data:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(new_data)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
