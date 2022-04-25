def kadanesAlgorithm(array):
    maxSoFar = maxEndAt = array[0]
    for i in array[1:]:
        maxEndAt = max(maxEndAt + i, i)
        maxSoFar = max(maxSoFar, maxEndAt)
    return maxSoFar
