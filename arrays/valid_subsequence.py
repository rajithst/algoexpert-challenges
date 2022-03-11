def isValidSubsequence(array, sequence):
    sequence_index = 0
    for i in range(len(array)):
        if sequence_index < len(sequence) and array[i] == sequence[sequence_index]:
            sequence_index += 1
    return sequence_index == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
