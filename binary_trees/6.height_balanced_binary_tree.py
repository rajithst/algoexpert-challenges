# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


def binaryTreeDiameter(tree):

    def dfs(node):
        if not node:
            return TreeInfo(0, 0)

        ll = dfs(node.left)
        rl = dfs(node.right)
        max_diameter = max(max(ll.diameter, rl.diameter), ll.height + rl.height)
        return_height = max(ll.height, rl.height) + 1
        return TreeInfo(return_height, max_diameter)

    return dfs(tree).diameter
