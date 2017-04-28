class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = next


def check_cycle(node):
    """Run through single-linked list, confirm if it cycles (return False if not), return data where cycle starts

    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(3)

    >>> a.nextnode = b
    >>> b.nextnode = c
    >>> c.nextnode = a

    >>> check_cycle(a)
    1
    """

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 is not None and marker2.nextnode is not None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            # Return True if the question asks if it is a cycle
            # return True

            # Check to see at which node the connect at, Floyd's Algorithm
            marker1 = node

            while marker1 != marker2:
                marker1 = marker1.next
                marker2 = marker2.next
            return marker1.data

    # Case where marker ahead reaches the end of the list
    return False


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
