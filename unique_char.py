def find_unique(s):
    """Given a string,determine if it is compreised of all unique characters.
    For example, the string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.

    >>> find_unique('abcde')
    True

    >>> find_unique('aabcde')
    False
    """
    if len(s) == 1:
        return True

    if s == '':
        return ""

    counter = {}

    # O(n)
    for item in s:
        counter[item] = counter.get(item, 0) + 1

    # O(n) iterate through a dictionary
    for key, value in counter.iteritems():
        if value > 1:
            return False

    return True


def find_uni_set(s):
    """Given a string,determine if it is compreised of all unique characters.
    For example, the string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.

    >>> find_unique('abcde')
    True

    >>> find_unique('aabcde')
    False
    """
    # O(n) to put each letter from s into set
    return len(set(s)) == len(s)


def find_uni(s):
    """Given a string,determine if it is compreised of all unique characters.
    For example, the string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.

    >>> find_unique('abcde')
    True

    >>> find_unique('aabcde')
    False
    """
    characters = set()

    # O(n)
    for letter in s:
        # O(1)
        if letter in characters:
            return False
        else:
            characters.add(letter)

    return True

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
