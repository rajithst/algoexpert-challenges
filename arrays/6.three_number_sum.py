def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for i in range(len(array) - 2):
        j = i + 1
        k = len(array) - 1
        while j < k:
            total = array[i] + array[j] + array[k]
            if total == targetSum:
                result.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif total > targetSum:
                k -= 1
            else:
                j += 1
    return result
