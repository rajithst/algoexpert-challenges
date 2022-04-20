def moveElementToEnd(array, toMove):
    # Write your code here.
    end_pointer = len(array) - 1
    start_pointer = 0
    while end_pointer >= start_pointer and array[end_pointer] == toMove:
        end_pointer -= 1
    while start_pointer < end_pointer:
        if array[start_pointer] == toMove:
            array[start_pointer], array[end_pointer] = array[end_pointer], array[start_pointer]
            end_pointer -= 1
            while end_pointer >= start_pointer and array[end_pointer] == toMove:
                end_pointer -= 1
        else:
            start_pointer += 1
    return array
