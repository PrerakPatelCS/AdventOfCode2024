from collections import deque

with open("Day10.txt", "r") as file:
    matrix = list(line.strip() for line in file)

n, m = len(matrix), len(matrix[0])
for i in range(n):
    matrix[i] = list(map(int, matrix[i]))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def check_bounds(x, y):
    return 0 <= x < n and 0 <= y < m


def all_trails(x, y):
    queue = deque([(x, y)])
    total = 0
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[x][y] = 1

    while queue:
        i, j = queue.pop()
        if matrix[i][j] == 9:
            total += 1
            continue
        for dx, dy in dirs:
            new_x, new_y = i + dx, j + dy
            if (
                check_bounds(new_x, new_y)
                and visited[new_x][new_y] == 0
                and matrix[new_x][new_y] - matrix[i][j] == 1
            ):
                visited[new_x][new_y] = 1
                queue.appendleft((new_x, new_y))

    return total


def puzzle1():
    total = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                total += all_trails(i, j)

    return total


def all_distinct_trails(x, y, visited):
    """
    dfs
    """
    if matrix[x][y] == 9:
        return 1
    total = 0
    visited[x][y] = 1

    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if (
            check_bounds(new_x, new_y)
            and visited[new_x][new_y] == 0
            and matrix[new_x][new_y] - matrix[x][y] == 1
        ):
            visited[new_x][new_y] = 1
            total += all_distinct_trails(new_x, new_y, visited)
            visited[new_x][new_y] = 0
    return total


def puzzle2():
    total = 0
    visited = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                total += all_distinct_trails(i, j, visited)

    return total


# print(puzzle1())  # 552
print(puzzle2())  #
