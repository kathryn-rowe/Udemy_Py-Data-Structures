def lg_cont_sum(arr):
    """"Given an array of integers (positive and negative) find the largest continuous sum.

    >>> lg_cont_sum([1,2,-1,3,4,10,10,-10,-1])
    29

    >>> lg_cont_sum([])
    0
    """

    if len(arr) == 0:
        return 0

    max_sum = 0
    total = arr[0]

    for num in arr[1:]:
        total += num
        if total > max_sum:
            max_sum = total

    # max_index = arr.index(
    #     max_sum)

    # cont_sum = arr[:max_index]

    # return cont_sum
    return max_sum

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
