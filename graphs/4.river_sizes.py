def riverSizes(matrix):
    # Write your code here.
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[0] * cols for col in range(rows)]

    def river_size(x, y, cell_count):
        visited[x][y] = 1
        cell_count.c = cell_count.c + 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for xx, yy in directions:
            newx = x + xx
            newy = y + yy
            if 0 <= newx < rows and 0 <= newy < cols and matrix[newx][newy] == 1 and visited[newx][newy] == 0:
                river_size(newx, newy, cell_count)

    result = []
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                cell_count = cellCount(0)
                river_size(i, j, cell_count)
                result.append(cell_count.c)
    return result


class cellCount:
    def __init__(self, c):
        self.c = c
