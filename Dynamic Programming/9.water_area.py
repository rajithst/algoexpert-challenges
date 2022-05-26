def waterArea(heights):
    # Write your code here.
    maxes = [0 for x in heights]
    left_max = 0
    # find max height for each index from left
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = left_max
        left_max = max(left_max,height)

    # find max height for each index from right
    # amount of water trap for each index is
    #  min(max_height_from_left,max_height_from_right)
    # if current index has a building which height is smaller it can hold the water
    #   |
    #   |  water=1                             |
    #   |...............|......................|
    #  left max=3    given index = 1      right max = 2
    right_max = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        min_height = min(right_max,maxes[i])
        # if current index building is shorter than left and right buildings
        if height < min_height:
            # water can trap
            maxes[i] = min_height - height
        else:
            # water can't trap
            maxes[i] = 0
        right_max = max(height,right_max)
    return sum(maxes)
