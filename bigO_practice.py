def sum1(n):
    """Take an input of n and return the sum of the numbers from 0 to n"""

    final_sum = 0
    for x in xrange(n+1):
        final_sum += x

    return final_sum


def sum2(n):
    """Take an input of n and return the sum of the numbers from 0 to n"""

    return (n*(n+1))/2


def print_1(lst):
    """Print through list one time, linear. O(n)"""

    # O(n)
    for word in lst:
        print word


def print_2(lst):
    """ Prints two times, O(2 x n). BUT as n approaches infinity, the 2 is negotiable
    because 2 x infinity is basically infinity."""

    # O(n)
    for word in lst:
        print word

    # O(n)
    for word in lst:
        print word


def printer(n):
    for x in range(n):   # Time complexity O(n)
        print "Hello World"   # Space complexity O(1)


def create_list(n):
    """the size of the new_list object scales with the input n,
    this shows that it is an O(n) algorithm with regards to space complexity."""

    new_list = []

    for num in range(n):
        new_list.append('new')

    return new_list


def print_while(n):
    """x is cut in half each time through the loop,
    so it will only take log(n) iterations"""

    x = n

    while x > 0:
        y = 2 + 2
        x = x // 2
