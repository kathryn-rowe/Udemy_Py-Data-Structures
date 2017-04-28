class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        # doubly linked list
        self.prev = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, data):
        """Find if the input data is in the list.

        >>> ll = LinkedList()
        >>> ll.append('dog')
        >>> ll.append('cat')
        >>> ll.append('fish')

        >>> ll.find('fish')
        True

        """
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def append(self, data):
        """Add an new node to the end of the list.
        >>> ll = LinkedList()
        >>> ll.append('dog')
        >>> ll.append('cat')
        >>> ll.append('fish')

        >>> ll.tail.data
        'fish'

        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):
        """Print each data item for each node in the LL.
        >>> ll = LinkedList()
        >>> ll.append('dog')
        >>> ll.append('cat')
        >>> ll.append('fish')

        >>> ll.print_list()
        dog
        cat
        fish
        """

        current = self.head

        while current:

            print current.data

            current = current.next

    def remove(self, data):
        """Remove node from LL if its data matches input.

        >>> ll = LinkedList()
        >>> ll.append('dog')
        >>> ll.append('cat')
        >>> ll.append('fish')

        >>> ll.remove('cat')
        >>> ll.print_list()
        dog
        fish
        """
        prev = None
        current = self.head

        while (current is not None) and (current.data != data):
            prev = current
            current = current.next

        if prev is None:
            prev = self.head
        else:
            prev.next = current.next

    def get_node_by_index(self, index):
        """Return Node from LL if its index matches input.

        >>> ll = LinkedList()
        >>> ll.append('dog')
        >>> ll.append('cat')
        >>> ll.append('fish')

        >>> ll.get_node_by_index(0)
        'dog'

        >>> ll.get_node_by_index(5)
        'Index not found'
        """

        current = self.head
        i = 0

        while (current is not None):
            if i == index:
                return current.data
            else:
                current = current.next
                i += 1

        return "Index not found"


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
