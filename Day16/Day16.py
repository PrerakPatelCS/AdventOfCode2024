import heapq
import itertools

with open("Day16.txt", "r") as file:
    matrix = list(list(line.strip()) for line in file)
    n, m = len(matrix), len(matrix[0])
    start, end = (), ()
    for i, j in itertools.product(range(n), range(m)):
        if matrix[i][j] == "S":
            start = (i, j)
        if matrix[i][j] == "E":
            end = (i, j)

vertical = {"S": (1, 0), "N": (-1, 0)}

horizontal = {"E": (0, 1), "W": (0, -1)}


def generate_neighbors(x, y, d, points):
    """
    Using yeild we can generate all the neighbors and return them
    """
    if d in ["E", "W"]:
        # Taking a turn
        for direction in vertical:
            new_x, new_y = x + vertical[direction][0], y + vertical[direction][1]
            if matrix[new_x][new_y] != "#":
                yield (
                    new_x,
                    new_y,
                    direction,
                    points + 1001,
                )
        new_x, new_y = x + horizontal[d][0], y + horizontal[d][1]
        if matrix[new_x][new_y] != "#":
            yield (
                new_x,
                new_y,
                d,
                points + 1,
            )
    else:
        # Taking a turn
        for direction in horizontal:
            new_x, new_y = x + horizontal[direction][0], y + horizontal[direction][1]
            if matrix[new_x][new_y] != "#":
                yield (
                    new_x,
                    new_y,
                    direction,
                    points + 1001,
                )
        new_x, new_y = x + vertical[d][0], y + vertical[d][1]
        if matrix[new_x][new_y] != "#":
            yield (
                new_x,
                new_y,
                d,
                points + 1,
            )


def puzzle1():
    """
    find the minimum cost to get from S to E.
    Start at S facing east and need to reach the end tile.
    turns are 1000 points and straight is 1 point.
    dijkstras
    Part2
    get all nodes that are part of a best path
    there are multiple of the best path.
    I prune them out from the visited.
    Get the points per coordinate in the best path.
    If I can get there a different way then we have another path.
    depending on the number of turns and straights we can prune heavily.
    We can do a dfs of all paths but pruned heavily knowing the best path.
    """
    min_heap = [(0, *start, "E", [(0, *start)])]
    visited = set()
    answers = []
    while min_heap:
        points, x, y, direction, p = heapq.heappop(min_heap)

        if (x, y) == end:
            answers = p
            break

        for new_x, new_y, new_d, new_points in generate_neighbors(
            x, y, direction, points
        ):
            if (new_d, new_x, new_y) not in visited:
                new_path = p[0:] + [(new_points, new_x, new_y)]
                heapq.heappush(
                    min_heap,
                    (new_points, new_x, new_y, new_d, new_path),
                )
                visited.add((new_d, new_x, new_y))

    for _, x, y in answers:
        matrix[x][y] = "O"

    for row in matrix:
        print("".join(row))

    return answers


def puzzle2(best_path):
    """
    Part 2 we need to find all paths that get from S to E with the same number
    of points as the best path from answers

    Make a function to get all valid tuples for the next iteration.
    Make a visited array where we get the minimum points to get there.
    If we get to that spot with more points we are not acceptable.

    """

    best_points = best_path[-1][0]
    best_turns, best_straights = best_points // 1000, best_points % 1000
    min_point = [[float("inf") for _ in range(m)] for _ in range(n)]

    for points, x, y in best_path:
        min_point[x][y] = points

    paths = []

    def dfs(x, y, d, points, visited):
        if (x, y) == end:
            paths.append(visited.copy())
            return

        # Pruning
        if points > best_points:
            return
        turns, straights = points // 1000, points % 1000
        if turns > best_turns or straights > best_straights:
            return
        # points remaining if you can go straight there
        manhattan_distance_points = (
            abs(end[0] - x)
            + abs(end[1] - y)
            + (0 if end[0] == x or end[1] == y else 1000)
        )
        if points + manhattan_distance_points > best_points:
            return

        min_point[x][y] = min(min_point[x][y], points)
        if points > min_point[x][y] + 1000:
            return

        for new_x, new_y, new_d, new_points in generate_neighbors(x, y, d, points):
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                dfs(new_x, new_y, new_d, new_points, visited)
                visited.remove((new_x, new_y))

    dfs(*start, "E", 0, set())
    matrix[start[0]][start[1]] = "O"
    all_paths = set(start)
    for path in paths:
        all_paths |= path
        for x, y in path:
            matrix[x][y] = "O"

    for row in matrix:
        print("".join(row))
    return len(all_paths) - 1


# print(puzzle1())
print(puzzle2(puzzle1()))  # Part 1 = 99488, Part 2 = 516
