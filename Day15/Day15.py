import itertools

with open("Day15.txt", "r") as file:
    matrix = []
    moves = []

    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == "#":
            matrix.append(list(line))
        else:
            moves += line


n, m = len(matrix), len(matrix[0])


def get_start(mat):
    for i, j in itertools.product(range(n), range(m)):
        if mat[i][j] == "@":
            return (i, j)
    return ()


start = get_start(matrix)


def in_bounds(x):
    i, j = x
    return 0 <= i < n and 0 <= j < m


dirs = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def calc_gps(mat):
    total = 0
    for i, j in itertools.product(range(n), range(m)):
        if mat[i][j] == "O" or mat[i][j] == "[":
            total += 100 * i + j
    return total


def print_matrix(mat):
    for row in mat:
        print("".join(row))


def add_coord(x, y):
    return (x[0] + y[0], x[1] + y[1])


def puzzle1():
    """
    move with the directions given.
    Move boxes, cannot move #.
    """

    def is_moveable(coord, move):
        coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        while in_bounds(coord) and matrix[coord[0]][coord[1]] == "O":
            coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        matrix[coord[0]][coord[1]] = "O"
        return True

    coord = start
    for move in moves:
        move = dirs[move]
        if is_moveable(coord, move):
            matrix[coord[0]][coord[1]] = "."
            coord = add_coord(coord, move)
            matrix[coord[0]][coord[1]] = "@"
        # print_matrix(matrix)

    return calc_gps(matrix)


def new_matrix():
    """
    If the tile is #, the new map contains ## instead.
    If the tile is O, the new map contains [] instead.
    If the tile is ., the new map contains .. instead.
    If the tile is @, the new map contains @. instead.
    """
    global matrix, m, start
    repl = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    new_matrix = [["" for i in range(m)] for j in range(n)]
    for i, j in itertools.product(range(n), range(m)):
        new_matrix[i][j] = repl[matrix[i][j]]

    for i, row in enumerate(new_matrix):
        new_matrix[i] = list("".join(row))
    m = len(new_matrix[0])
    matrix = new_matrix
    for i, j in itertools.product(range(n), range(m)):
        if matrix[i][j] == "@":
            start = (i, j)

    print_matrix(matrix)


def puzzle2():
    """
    Transform the map to be 2x wide.
    Pushing boxes left and right is normal.
    Up and down can be tricky
    """
    new_matrix()

    def is_moveable(coord, move):
        if move in "<>":
            return horizontal_move(coord, dirs[move])
        else:
            return vertical_move(coord, dirs[move])
        """
        coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        while in_bounds(coord) and matrix[coord[0]][coord[1]] in "[]":
            coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        matrix[coord[0]][coord[1]] = "O"
        return True
        """

    def horizontal_move(coord, move):
        initial_col = coord[1]
        coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        while in_bounds(coord) and matrix[coord[0]][coord[1]] in "[]":
            coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        prev = ""
        for j in range(initial_col + 1, coord[1] + move[1], move[1]):
            if prev == "":
                prev = matrix[coord[0]][j]
                continue
            matrix[coord[0]][j], prev = prev, matrix[coord[0]][j]
        return True

    def vertical_move(coord, move):
        """
        DFS to find if we can move.
        and then another dfs to do the move.
        we need the initial dfs because we cannot start moving until
        all leaf nodes are checked and are acceptable to be moved.

        """
        coord = add_coord(coord, move)
        if not in_bounds(coord) or matrix[coord[0]][coord[1]] == "#":
            return False
        if matrix[coord[0]][coord[1]] == ".":
            return True

        return False

    coord = start
    for move in moves:
        if is_moveable(coord, move):
            matrix[coord[0]][coord[1]] = "."
            coord = add_coord(coord, dirs[move])
            matrix[coord[0]][coord[1]] = "@"
        print_matrix(matrix)

    return calc_gps(matrix)


# print(puzzle1())  # 1465152

print(puzzle2())  #
