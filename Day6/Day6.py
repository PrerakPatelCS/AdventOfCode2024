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
    visited = set()
    coord = start
    dir = complex(-1, 0)
    while coord in coords:
        if coords[coord] == "#":
            coord -= dir
            dir = right[dir]
        else:
            visited.add(coord)
            coord += dir

    return len(visited)


def is_cycle(x):
    visited = set()
    coord = start
    dir = complex(-1, 0)
    while coord in coords:
        if coords[coord] == "#" or coord == x:
            coord -= dir
            dir = right[dir]
        else:
            if (coord, dir) in visited:
                return True
            visited.add((coord, dir))
            coord += dir

    return False


def possible_spots():
    """
    Make a list of coordinates that could make a cycle
    """
    visited = set()
    coord = start
    dir = complex(-1, 0)
    while coord in coords:
        if coords[coord] == "#":
            coord -= dir
            dir = right[dir]
        else:
            visited.add(coord)
            coord += dir

    return visited


def puzzle2():
    """
    we can do is_cycle() for every change we do.
    is cycle is easy, if we reach the same point with the same direction it is a cycle.
    we only need to put an object on a block that the guard will pass through.
    Further we only want to put a block if we know that it will hit another block
    after turning right.
    """
    return sum(is_cycle(x) for x in possible_spots())


# print(puzzle1())  # 4454
print(puzzle2())  # 1503
