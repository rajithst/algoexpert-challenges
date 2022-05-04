def mergeOverlappingIntervals(intervals):
    # sort by starting value to find starting slot
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # get first pair as starting values
    start = sorted_intervals[0][0]
    end = sorted_intervals[0][1]
    results = []

    # iterate from next pair
    for i in range(1, len(sorted_intervals)):
        current_start, current_end = sorted_intervals[i]

        # if current start time <= end --> update end
        if current_start <= end:
            end = max(end, current_end)
        # if not overlapping,add calculated start,end to result
        # update start and end to current values
        else:
            results.append([start, end])
            start, end = current_start, current_end
    results.append([start, end])


    return results
