def longestPeak(array):
    # Write your code here.
    i = 1
    j = len(array) - 1
    longest_peak = float("-inf")
    for i in range(i, j):
        # iterate and find the peak
        if array[i - 1] < array[i] > array[i + 1]:
            i1 = i
            i2 = i
            c1 = 0
            # from the peak,go right and left till end of the slope
            while i1 > 0 and array[i1] > array[i1 - 1]:
                i1 -= 1
                c1 += 1
            while i2 < j and array[i2] > array[i2 + 1]:
                i2 += 1
                c1 += 1
            # count the slop of right and left and keep max length
            longest_peak = max(longest_peak, c1 + 1)
    return longest_peak if longest_peak != float("-inf") else 0
