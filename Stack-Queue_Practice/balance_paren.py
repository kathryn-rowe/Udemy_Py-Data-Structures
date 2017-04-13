def balance_paren(s):
    """Given a string of opening and closing parentheses, check whether it is balanced."""

    if s == "":
        return ""

    if len(s) % 2 != 0:
        return False

    # create stack for each symbol
    parens = []
    brackets = []
    curly = []

    for item in s:
        if item == "(":
            parens.append(item)
        elif item == "[":
            brackets.append(item)
        elif item == "{":
            curly.append(item)
        elif item == ")":
            if len(parens) == 0:
                return False
            else:
                parens.pop()
        elif item == "]":
            if len(brackets) == 0:
                return False
            else:
                brackets.pop()
        elif item == "}":
            if len(curly) == 0:
                return False
            else:
                curly.pop()

    total_len = len(parens) + len(brackets) + len(curly)

    if total_len > 0:
        return False

    return True


def balance_check(s):

    # Check is even number of brackets
    if len(s) % 2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')
    closing = set(')]}')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for paren in s:

        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)

        else:

            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False

            # if there are more characters other than paren, brackets, curly
            if paren in closing:
                # Check the last open parenthesis
                last_open = stack.pop()

                # Check if it has a closing match
                if (last_open, paren) not in matches:
                    return False

    return len(stack) == 0

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
import unittest


class TestBalanceCheck(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(balance_check('[](){([[[]]])}('), False)
        self.assertEqual(balance_check('[{{{(())}}}]((()))'), True)
        self.assertEqual(balance_check('[[[]])]'), False)
        self.assertEqual(balance_paren('[](){([[[]]])}('), False)
        self.assertEqual(balance_paren('[{{{(())}}}]((()))'), True)
        self.assertEqual(balance_paren('[[[]])]'), False)
        print 'ALL TEST CASES PASSED'

# Run Tests

if __name__ == '__main__':
    unittest.main()
