def isMonotonic(array):
    # Write your code here.
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if direction > 0:
            if array[i] - array[i - 1] < 0:
                return False
        else:
            if array[i] - array[i - 1] > 0:
                return False
    return True
