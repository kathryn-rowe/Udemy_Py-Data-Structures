def rev_sent(sent):
    """Given a string of words, reverse all the words.

    >>> rev_sent('This is the best')
    'best the is This'

    >>> rev_sent('  space here'  and 'space here      ')
    'here space'
    """

    sent = sent.split(" ")

    open_sent = ""

    for word in sent[::-1]:
        open_sent = open_sent + " " + word

    return open_sent.lstrip().rstrip()


def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    >>> rev_word3('This is the best')
    'best the is This'

    >>> rev_word3('  space here'  and 'space here      ')
    'here space'
    """

    words = []
    # spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < len(s):

        # If element isn't a space
        if s[i] != " ":

            # The word starts at this index
            word_start = i

            while i < len(s) and s[i] != " ":

                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
