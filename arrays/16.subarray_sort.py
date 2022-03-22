def subarraySort(array):
    # Write your code here.
    smallest = float("inf")
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            smallest = min(smallest, array[i])

    largest = float("-inf")
    for i in range(len(array) - 2, -1, -1):
        if array[i] > array[i + 1]:
            largest = max(largest, array[i])

    if smallest == float("inf") or largest == float("inf"):
        return [-1, -1]
    p1 = 0
    while smallest >= array[p1]:
        p1 += 1

    p2 = len(array) - 1
    while largest <= array[p2]:
        p2 -= 1
    return [p1, p2]


print(subarraySort([2,1,2]))
