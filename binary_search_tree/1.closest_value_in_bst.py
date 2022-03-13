def findClosestValueInBst(tree, target):
    def dfs(node, closest, target):

        # if it is a leaf node or,found end,which means can't find any closer node
        # return current closest value
        if not node:
            return closest
        # everytime,try to update closest value by comparing diff
        if abs(closest - target) > abs(node.value - target):
            closest = node.value

        # if node value is greater than target,go to left subtree
        if node.value > target:
            return dfs(node.left, closest, target)
        # if node value is less than target,go to right subtree
        elif node.value < target:
            return dfs(node.right, closest, target)
        # if node value is equal to target,return the value
        else:
            return node.value

    return dfs(tree, tree.value, target)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
