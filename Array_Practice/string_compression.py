def compress_string(s):
    """Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
    For this problem, you can falsely "compress" strings of single or double letters.
    For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

    >>> compress_string('AAAAABBBBCCCC')
    'A5B4C4'

    >>> compress_string('AAAaaa')
    'A3a3'
    """
    letter_count = {}
    compress_string = ""

    for item in s:
        letter_count[item] = letter_count.get(item, 0) + 1

    for key, value in letter_count.iteritems():
        compress_string = compress_string + key + str(value)

    # will return an unsorted string with letter:count pair
    return compress_string


def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.

    >>> compress_string('AAAAABBBBCCCC')
    'A5B4C4'

    >>> compress_string('AABBC')
    'A2B2C1'

    >>> compress_string('AAAaaa')
    'A3a3'
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    #Intialize Values
    # last = s[0]
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    # r = r + s[i - 1] + str(cnt)

    return r

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
