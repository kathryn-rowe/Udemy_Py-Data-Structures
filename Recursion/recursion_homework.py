def rec_sum(n):
    """Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
    >>> rec_sum(4)
    10
    """
    if n == 0:
        return 0
    else:
        sum = n + rec_sum(n - 1)

    return sum


def sum_func(n):
    """Given an integer, create a function which returns the sum of all the individual digits in that integer.
    4502 % 10 + sum_func(4502/10)

    >>> sum_func(4321)
    10
    """
    if n == 0:
        return 0
    else:
        sum = n % 10 + sum_func(n/10)

    return sum


def word_split(phrase, list_of_words, output=None):
    """Create a function called word_split() which takes in a string phrase and a set list_of_words.
    The function will then determine if it is possible to split the string in a way in which words can be
    made from the list of words. You can assume the phrase will only contain words found in the dictionary
    if it is completely splittable.
    >>> word_split('themanran',['the','ran','man'])
    ['the', 'man', 'ran']
    >>> word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
    ['i', 'love', 'dogs', 'John']
    >>> word_split('themanran',['clown','ran','man'])
    []

    """
    if output is None:
        output = []

    # For every word in list
    for word in list_of_words:

        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):

            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):], list_of_words, output)

    # Finally return output if no phrase.startswith(word) returns True
    return output


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
