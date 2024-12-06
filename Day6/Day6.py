with open("Day6.txt", "r") as file:
    matrix = [line[:-1] for line in file]

    start = (0, 0)
    coords = {}
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == "^":
                start = (i, j)
            coords[(i, j)] = matrix[i][j]


right = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
n, m = len(matrix), len(matrix[0])
print(n, m, start)


def puzzle1():
    visited = [[0 for col in row] for row in matrix]
    coord = start
    dir = (-1, 0)
    while coord in coords:
        visited[coord[0]][coord[1]] = 1
        if coords[coord] == "#":
            visited[coord[0]][coord[1]] = 0
            newX = coord[0] - dir[0]
            newY = coord[1] - dir[1]
            coord = (newX, newY)
            dir = right[dir]
        newX = coord[0] + dir[0]
        newY = coord[1] + dir[1]
        coord = (newX, newY)

    return sum(sum(row) for row in visited)


print(puzzle1())  # 4454
