def nonConstructibleChange(coins):
    # Write your code here.
    coins = sorted(coins)
    prefix_sum = 0
    for i in range(len(coins)):
        if coins[i] > prefix_sum + 1:
            return prefix_sum + 1
        else:
            prefix_sum += coins[i]

    return prefix_sum + 1
