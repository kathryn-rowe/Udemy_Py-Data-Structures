class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = next


def reverse_linkedlist(node):
    """With the input node, reverse the linked list in place.
    Space 0(1)
    Time O(n)"""

    current = node
    previous = None
    next = None

    while current:
        # Saving the next node to go to
        next = current.next

        # Pointing the arrow in the opposite direction
        current.next = previous

        # Setting the node it is on to previous
        previous = current

        # Moving to the next node (changing which node is current)
        current = next

    return previous
