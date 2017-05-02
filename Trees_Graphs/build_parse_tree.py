from pythonds.basic.stack import stack
from pythonds.trees.binaryTree import binaryTree


def build_parse_tree(math_exp):
    expressions = math_exp.split()
    pStack = stack()
    eTree = binaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in expressions:
        # start of a grouping, create a left child, save the current node on the stack, move to left child
        if i == "(":
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        # if value is a number, save the number to a child, move back up to parent
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        # if it's an expression, set the value, create a right child, save the parent on the stack
        elif i in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

parse_tree = build_parse_tree("((10+5)*3)")
