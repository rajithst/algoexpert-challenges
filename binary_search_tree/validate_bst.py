class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(node, lower, upper):
    if node is None:
        return True
    # if current node value not in the given range,it's not satisfying bst property
    if node.value < lower or node.value >= upper:
        return False
    return dfs(node.left, lower, node.value) and dfs(node.right, node.value, upper)


