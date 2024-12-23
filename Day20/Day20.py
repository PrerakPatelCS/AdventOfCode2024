import itertools
from collections import deque

with open("Day20.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]
    n, m = len(matrix), len(matrix[0])
    start, end = (), ()
    CHEAT_TIME = 20
    for i, j in itertools.product(range(n), range(m)):
        if matrix[i][j] == "S":
            start = (i, j)
        if matrix[i][j] == "E":
            end = (i, j)


def print_matrix(mat):
    for row in mat:
        print("".join(row))


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_timed_matrix(mat):
    timed_matrix = [[0 for _ in range(m)] for _ in range(n)]
    # BFS to get the shortest path
    queue = [start]
    level = 1
    while queue:
        size = len(queue)
        new_queue = []
        for _ in range(size):
            x, y = queue.pop()
            # neighbors
            for i, j in dirs:
                new_x, new_y = x + i, y + j
                if (
                    0 <= new_x < n
                    and 0 <= new_y < m
                    and timed_matrix[new_x][new_y] == 0
                    and mat[new_x][new_y] != "#"
                    and mat[new_x][new_y] != "S"
                ):
                    new_queue.append((new_x, new_y))
                    timed_matrix[new_x][new_y] = level

        queue = new_queue
        level += 1

    return timed_matrix


def manhattan(x, y, new_x, new_y):
    return abs(x - new_x) + abs(y - new_y)


def all_end_points(x, y):
    for i, j in itertools.product(
        range(-CHEAT_TIME, CHEAT_TIME + 1), range(-CHEAT_TIME, CHEAT_TIME + 1)
    ):
        if abs(i) + abs(j) <= CHEAT_TIME and 0 <= x + i < n and 0 <= y + j < m:
            yield (x + i, y + j)


def puzzle1(time_wanted=100):
    """
    Assuming there is only 1 path from the start to the end.
    make a matrix that records what time you get there and
    every cheat can be calculated with regards to that.
    We need to look at every single cheat to know how many are above 100.
    Using a cheat on a free space saves 0 seconds.
    For ever wall neighbor we want to check how much time we save
    we save the most if we can get to the highest point after breaking a wall.
    So return the max neighbor of that wall we broke.
    If we want to break more walls we need to recursively do that.
    how many walls we go through we need to account for that.
    only 2 is possible for puzzle 1.
    Each cheat has a distinct start and end position.
    Go though the path, at each point on the path find every distinct cheat.
    Find every manhattan distance of 2 away from the current point.
    just find the end points, don't need to do a dfs.
    All cheat end points will be a rombus around the point.
    """
    timed_matrix = get_timed_matrix(matrix)
    # Go through the path
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([start])
    ans = 0
    while queue:
        x, y = queue.popleft()
        # Find all cheat end points
        for new_x, new_y in all_end_points(x, y):
            if (
                matrix[new_x][new_y] == "#"
                or timed_matrix[new_x][new_y] < timed_matrix[x][y]
            ):
                continue
            time_saved = (
                timed_matrix[new_x][new_y]
                - (manhattan(x, y, new_x, new_y))
                - timed_matrix[x][y]
            )
            if time_saved >= time_wanted:
                ans += 1

        # neighbors
        for i, j in dirs:
            new_x, new_y = x + i, y + j
            if (
                0 <= new_x < n
                and 0 <= new_y < m
                and visited[new_x][new_y] == 0
                and matrix[new_x][new_y] != "#"
                and matrix[new_x][new_y] != "S"
            ):
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1

    return ans


# get_timed_matrix(matrix)
# all_end_points(*start)
# print(puzzle1())  # Cheat time = 2 and answer = 1395
print(puzzle1())  # Cheat time = 20 and answer = 993178
