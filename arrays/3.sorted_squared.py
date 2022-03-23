def sortedSquaredArray(array):
    # Write your code here.

    # biggest squared value will be lowest minus value or biggest positive value
    # since array is sorted.first and last value will be give the biggest sorted value
    # compare two values and place biggest value end of the result value
    # keep compare the ends till pointers meet in the middle
    left_pointer, right_pointer = 0, len(array) - 1
    result = [0] * len(array)
    counter = len(array) - 1
    while left_pointer <= right_pointer:
        left_val = array[left_pointer]
        right_val = array[right_pointer]
        if left_val * left_val >= right_val * right_val:
            result[counter] = left_val * left_val
            left_pointer += 1
        else:
            result[counter] = right_val * right_val
            right_pointer -= 1
        counter -= 1
    return result
