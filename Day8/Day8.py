from collections import defaultdict

with open("Day8.txt", "r") as file:
    matrix = [list(line[:-1]) for line in file]

    coords = {}
    antennas = defaultdict(list)
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            coord = complex(i, j)
            if col != ".":
                antennas[col].append(coord)
            coords[coord] = matrix[i][j]


def puzzle2():
    """
    go through every antenna list and then through every combination get all the antinodes
    """
    antinodes = set()
    for c in antennas:
        n = len(antennas[c])
        for i, node in enumerate(antennas[c]):
            antinodes.add(node)
            for j in range(i + 1, n):
                node2 = antennas[c][j]
                slope1 = node - node2
                slope2 = slope1 * -1
                antinode1 = node + slope1
                antinode2 = node2 + slope2
                # Puzzle 2 turn the if to while

                while antinode1 in coords:
                    antinodes.add(antinode1)
                    antinode1 += slope1
                while antinode2 in coords:
                    antinodes.add(antinode2)
                    antinode2 += slope2

    return len(antinodes)


# print(puzzle1())  # 354
print(puzzle2())  # 1263
