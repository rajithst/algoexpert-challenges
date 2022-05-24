def minHeightBst(array):
    start = 0
    end = len(array) - 1

    def create(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = BST(array[mid])
        root.left = create(start, mid - 1)
        root.right = create(mid + 1, end)
        return root

    return create(start, end)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)