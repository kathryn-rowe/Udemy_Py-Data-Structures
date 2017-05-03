class Node(object):

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?
        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )
        >>> t.is_balanced()
        True
        >>> t = Node(4,
        ...       Node(2, Node(3), Node(3)),
        ...       Node(6, Node(5))
        ... )
        >>> t.is_balanced()
        False
        """

        def _num_descendants(node):
            """Returns number of descendants or None if already imbalanced."""

            if not node:
                # Our base case: we're not a real node (child of a leaf)
                return 0

            # Get descendants on left; if "None", already imbalanced---bail out
            left = _num_descendants(node.left)

            if left is None:
                return None

            # Get descendants on right; if "None", already imbalanced---bail out
            right = _num_descendants(node.right)

            if right is None:
                return None

            if abs(left - right) > 1:
                # Heights vary by more than 1 -- imbalanced!
                return None

            # Height of this node is height of our deepest descendant + ourselves
            return max(left, right) + 1

        return _num_descendants(self) is not None

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
