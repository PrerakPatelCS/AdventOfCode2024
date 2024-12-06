with open("Day6.txt", "r") as file:
    matrix = [line[:-1] for line in file]

    start = (0, 0)
    coords = {}
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == "^":
                start = complex(i, j)
            coords[complex(i, j)] = matrix[i][j]


right = {
    complex(0, 1): complex(1, 0),
    complex(1, 0): complex(0, -1),
    complex(0, -1): complex(-1, 0),
    complex(-1, 0): complex(0, 1),
}


def puzzle1():
    count = 0
    coord = start
    dir = complex(-1, 0)
    while coord in coords:
        if coords[coord] == "#":
            coord -= dir
            dir = right[dir]
        else:
            coord += dir
            count += 1

    return count


print(puzzle1())  # 4454
