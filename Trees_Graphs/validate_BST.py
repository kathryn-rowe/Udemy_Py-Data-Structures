class Node(object):

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def is_valid(self):
        """Binary search tree node.
        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )
        >>> t.is_valid()
        True
        >>> t = Node(4,
        ...       Node(2, Node(3), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )
        >>> t.is_valid()
        False
        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(1), Node(7))
        ... )
        >>> t.is_valid()
        False
        """
        # LONG RUNTIME
        # values = [n.data for n in self]

        # return tree_vals == sorted(tree_vals)

        def _ok(n, lt, gt):
            """Check this node & recurse to children

                lt: left children must be <= this
                gt: right child must be >= this
            """
            # goes all the way to a leaf
            if n is None:
                return True

            if lt is not None and n.data > lt:
                return False

            if gt is not None and n.data < gt:
                return False

            # check left children
            if not _ok(n.left, n.data, gt):
                return False

            # check right children
            if not _ok(n.right, lt, n.data):
                return False

            return True

        return _ok(self, None, None)

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
