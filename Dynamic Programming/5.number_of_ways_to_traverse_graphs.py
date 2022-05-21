def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    memo = {}

    def solve(i, j):
        if i == width - 1 and j == height - 1:
            return 1
        if i >= width or j >= height:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        ways = solve(i + 1, j) + solve(i, j + 1)
        memo[(i, j)] = ways
        return ways

    return solve(0, 0)
