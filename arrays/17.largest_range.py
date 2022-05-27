def largestRange(array):
    # initialize variables
    largest_range = 0
    result = []
    mem = {}
    # store values in a map to track processed values
    for i in array:
        mem[i] = True
    # iterate through each value and cover the range left and right
    for i in array:
        # if value is already checked,continue to next
        if not mem[i]:
            continue
        mem[i] = False
        # from current value,expand to left and right to find the range
        current_length = 1
        prev_val = i - 1
        next_val = i + 1
        while prev_val in mem:
            mem[prev_val] = False
            current_length += 1
            prev_val -= 1

        while next_val in mem:
            mem[next_val] = False
            current_length += 1
            next_val += 1
        if current_length > largest_range:
            largest_range = current_length
            result = [prev_val + 1, next_val - 1]
    return result
