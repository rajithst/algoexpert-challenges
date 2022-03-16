# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # using dfs
    def dfs(node, branch_sum, results):
        if not node:
            return

        # create branch sum while traversing
        branch_sum += node.value
        dfs(node.left, branch_sum, results)
        dfs(node.right, branch_sum, results)
        # if current node is a leaf node,append branch sum to results array
        if node.left is None and node.right is None:
            results.append(branch_sum)

        # reduce sum while backtracking
        branch_sum -= node.value

    results = []
    dfs(root, 0, results)
    return results
