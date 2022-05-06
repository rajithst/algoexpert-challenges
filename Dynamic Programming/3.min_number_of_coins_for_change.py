def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    memo = {}

    def solve(amount):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        min_coins = float("inf")
        for coin in denoms:
            if amount - coin >= 0:
                min_coins = min(min_coins, solve(amount - coin) + 1)
        memo[amount] = min_coins
        return min_coins

    res = solve(n)
    return -1 if res == float("inf") else res
