def find_miss_num(arr1, arr2):
    """Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
    Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

    This solution can run into overflow problem if the number is too large or too small. Can loose information.

    >>> find_miss_num([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    5 is the missing number

    >>> find_miss_num([5,5,7,7],[5,7,7])
    5 is the missing number
    """

    total1 = 0
    for num in arr1:
        total1 += num

    total2 = 0
    for num in arr2:
        total2 += num

    miss_num = (max(total1, total2) - min(total1, total2))

    print "%s is the missing number" % (miss_num)


def finder(arr1, arr2):
    """
    >>> finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    5

    >>> finder([5,5,7,7],[5,7,7])
    5
    """

    # Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    # Otherwise return last element
    return arr1[-1]


from collections import defaultdict


def finder2(arr1, arr2):
    """
    >>> finder2([5,5,7,7], [5,7,7])
    5

    """

    # Using default dict to avoid key errors
    d = defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        d[num] += 1

    # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num

        # Otherwise, subtract a count
        else:
            d[num] -= 1


def finder3(arr1, arr2):
    """
    >>> finder3([5,5,7,7], [5,7,7])
    5

    """
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in (arr1 + arr2):
        result ^= num

    return result

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
