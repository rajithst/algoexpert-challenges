def maxSubsetSumNoAdjacent(array):
    # dp bottom up
    n = len(array)
    if n == 0:
        return 0
    if n == 1:
        return array[0]
    if n == 2:
        return max(array)

    dp = [0] * n
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, n):
        # if we include current value,max subset = current val + max till 2 index behind
        current_include = array[i] + dp[i - 2]
        # if we exclude current value,max subset = max till previous index
        current_exclude = dp[i - 1]

        # max till current = max of both
        dp[i] = max(current_include, current_exclude)
    return dp[n - 1]
