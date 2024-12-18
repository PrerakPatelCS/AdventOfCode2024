import itertools

with open("Day18.txt", "r") as file:
    n, m = 71, 71
    bytes = []
    for line in file:
        bytes.append(list(map(int, line.split(","))))


def print_matrix(mat):
    for row in mat:
        print("".join(row))


def puzzle1(num_bytes=1024):
    """
    The bytes are falling down, you are at (0, 0) and you need to get
    to (n-1, m-1)
    """
    mat = [["." for _ in range(m)] for _ in range(n)]
    # Add bytes to grid
    for i in range(num_bytes):
        x, y = bytes[i]
        mat[y][x] = "#"

    # BFS to get the shortest path
    queue = [(0, 0)]
    level = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    while queue:
        size = len(queue)
        new_queue = []
        for _ in range(size):
            x, y = queue.pop()
            if (x, y) == (n - 1, m - 1):
                return level
            # neighbors
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + i, y + j
                if (
                    0 <= new_x < n
                    and 0 <= new_y < m
                    and visited[new_x][new_y] == 0
                    and mat[new_x][new_y] != "#"
                ):
                    new_queue.append((new_x, new_y))
                    visited[new_x][new_y] = 1

        queue = new_queue

        level += 1

    return -1


def puzzle2():
    """
    First coordinate that makes the exit unreachable.
    """
    low, high = 0, len(bytes) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if puzzle1(num_bytes=mid) == -1:
            high = mid - 1
        else:
            low = mid + 1

    return bytes[high]


# print(puzzle1())
print(puzzle2())
"""
Interesting Union Find soltion.
Use union find on the falling bytes.
Connect them 8 directionally.
If top and bottom or left and right or bottom and right or top and left
are connected then we cannot reach the end.
"""
