def isValidSubsequence_1(array, sequence):
    sequence_index = 0
    for i in range(len(array)):
        if sequence_index < len(sequence) and array[i] == sequence[sequence_index]:
            sequence_index += 1
    return sequence_index == len(sequence)


def isValidSubsequence_2(array, sequence):
    # Write your code here.
    p1 = p2 = 0
    n1 = len(array)
    n2 = len(sequence)
    # subsequence ====> numbers that aren't necessarily adjacent but that are in the same order
    # increase sequence pointer,when value found
    # increase array pointer,while moving forward
    # finally check sequnece pointer is at the end of the sequence
    # if sequence pointer at the end,valid subsequence found
    while p1 < n1 and p2 < n2:
        if array[p1] == sequence[p2]:
            p2 += 1
        p1 += 1
    return p2 == n2


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence_1(array, sequence))
print(isValidSubsequence_2(array, sequence))
