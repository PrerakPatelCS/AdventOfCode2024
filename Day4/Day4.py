with open("Day4.txt", "r") as file:
    matrix = list(file)

n, m = len(matrix), len(matrix[0])
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def check_out_bounds(i, j):
    return i < 0 or i >= n or j < 0 or j >= m


def puzzle1():
    """
    find an X and then do a straight dfs in all 8 directions
    """
    target = "XMAS"

    def dfs(i, j, x, y):
        for letter in target:
            if check_out_bounds(i, j) or matrix[i][j] != letter:
                return 0
            i += x
            j += y

        return 1

    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target[0]:
                for x, y in dirs:
                    count += dfs(i, j, x, y)

    return count


def puzzle2():
    """
    find "A" and then check the corners so theres two MAS and MAS crossing
    """

    def check(i, j):
        diagonal_dirs = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        prev = ""
        for k, (x, y) in enumerate(diagonal_dirs):
            curr = matrix[i + x][j + y]
            if curr not in "MS":
                return 0
            if k % 2 == 0:
                prev = curr
            elif prev == curr:
                return 0

        return 1

    count = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == "A":
                count += check(i, j)

    return count


# print(puzzle1())  # 2571
print(puzzle2())  # 1992
