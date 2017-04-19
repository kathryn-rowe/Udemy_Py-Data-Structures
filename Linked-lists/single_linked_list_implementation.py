class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        # doubly linked list
        self.prev = None


# if __name__ == "__main__":
#     print
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "*** ALL TESTS PASSED ***"
#     print
