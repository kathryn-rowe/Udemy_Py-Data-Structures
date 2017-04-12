def check_anagram(sent1, sent2):
    """Looks at both sentences and sees if they are anagrams

    >>> check_anagram('clint eastwood','old west action')
    True

    >>> check_anagram('dd','aa')
    False
    """

    # removes spaces and makes sure both sentences are lower case
    sent1 = sent1.replace(' ', '').lower()
    sent2 = sent2.replace(' ', '').lower()

    # fast win
    if len(sent1) != len(sent2):
        return False

    # create counting dictionary. Add in all letters from sent 1, remove all letters
    # from sent 2. if nothing's left, they're equal!
    sent_count = {}

    for letter in sent1:
        # if letter in sent_count:
        #     sent_count[letter] += 1
        # else:
        #     sent_count[letter] = 1
        sent_count[letter] = sent_count.get(letter, 0) + 1

    for letter in sent2:
        # if letter in sent_count:
        #     sent_count[letter] -= 1
        # else:
        #     sent_count[letter] = 1
        sent_count[letter] = sent_count.get(letter, 0) - 1

    for count in sent_count:
        if sent_count[count] != 0:
            return False

    return True


def anagram(s1, s2):
    """Looks at both sentences and sees if they are anagrams

    >>> check_anagram('clint eastwood','old west action')
    True

    >>> check_anagram('dd','aa')
    False
    """

    # removes spaces and makes sure both sentences are lower case
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
