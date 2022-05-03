def arrayOfProducts(array):
    # Write your code here.
    right_mul = [1] * len(array)

    for i in range(1, len(array)):
        right_mul[i] = right_mul[i - 1] * array[i - 1]

    left_mul = [1] * len(array)
    for i in range(len(array) - 2, -1, -1):
        left_mul[i] = left_mul[i + 1] * array[i + 1]

    result = []
    for i in range(len(array)):
        result.append(right_mul[i] * left_mul[i])
    return result
