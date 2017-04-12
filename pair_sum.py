def pair_sum(lst, k):
    """Given an integer array, output all the unique pairs that sum up to a specific value k.

    >>> pair_sum([2,4,1,3],5)
    set([(2, 3), (1, 4)])

    """

    if len(lst) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in lst:

        # Set target difference
        target = k-num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target),  max(num, target)))

    return output

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
