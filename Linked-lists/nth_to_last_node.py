class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        # doubly linked list
        self.prev = None


def nth_to_last_node(n, head):
    """Takes a head node and an integer value n and then returns the nth to last node in the linked list.
    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(3)
    >>> d = Node(4)
    >>> e = Node(5)

    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = e

    >>> target_node = nth_to_last_node(2, a)

    >>> target_node.data
    4
    """

    marker1 = head
    marker2 = head

    for i in xrange(n-1):

        if marker1.next is None:
            return "Error: no idex value"

        marker1 = marker1.next

    while marker1.next:
        marker1 = marker1.next
        marker2 = marker2.next

    return marker2

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
