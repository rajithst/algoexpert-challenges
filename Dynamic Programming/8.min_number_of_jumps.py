def minNumberOfJumps(array):
    # Write your code here.
    memo = {}

    def solve(i):
        if i == len(array) - 1:
            return 0
        if i >= len(array):
            return float("inf")
        if i in memo:
            return memo[i]

        min_steps = float("inf")
        for step in range(1, array[i] + 1):
            min_steps = min(min_steps, solve(i + step) + 1)
        memo[i] = min_steps
        return min_steps

    return solve(0)
