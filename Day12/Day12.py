import itertools
from collections import deque

with open("Day12.txt", "r") as file:
    matrix = [line.strip() for line in file]
    coords = {}
    n, m = len(matrix), len(matrix[0])
    for i, j in itertools.product(range(n), range(m)):
        coords[complex(i, j)] = matrix[i][j]


def part2(region_nodes):
    """
    Count Corners
    Outside corner if both a horizontal and vertical neighbor is out of bounds or another region
    Inside corner if both a horizontal and vertical neighbor is the same region and the diagonal between them is another region
    """
    corners = 0
    horizontal, vertical = [complex(0, 1), complex(0, -1)], [
        complex(1, 0),
        complex(-1, 0),
    ]
    for node in region_nodes:
        for h, v in itertools.product(horizontal, vertical):
            # h + v is the diagonal between the two
            horizontal_fence, vertical_fence, diagonal = False, False, False
            if node + h not in coords or node + h not in region_nodes:
                horizontal_fence = True
            if node + v not in coords or node + v not in region_nodes:
                vertical_fence = True
            if node + h + v not in coords or node + h + v not in region_nodes:
                diagonal = True

            # Outside Corners
            if horizontal_fence and vertical_fence:
                corners += 1
            # Inside Corners
            elif not horizontal_fence and not vertical_fence and diagonal:
                corners += 1

    return corners


def puzzle1():
    """
    Find area and perimeter of each region.
    Area = Num squares
    Perimeter = Number of outter sides of the region
    Price = Area * Perimeter
    Total Price = sum of all prices of each region
    Part 2 perimeter calc is for each long side
    we can use corners to calc the new perimeter
    the problem is the inside corners
    AAAA
    ABBA
    ABBA
    AAAA
    A has 8 corners and 8 sides but the inside corners are hard to calc.
    To get inside corners we need to check all 8 directions
    inside corner if
    ab
    aa
    Inside corner if
    AAAAAA
    AAABBA
    AAABBA
    ABBAAA
    ABBAAA
    AAAAAA
    the 2 A's in the middle make 2 different corners but we don't even know if they are part of the same region so we can't do the inside corner check at that time.
    We would need to do a second pass.
    """
    visited = set()

    def bfs(x):
        nonlocal visited
        area, perimeter = 1, 0
        queue = deque([x])
        region = coords[x]
        region_nodes = set()
        region_nodes.add(x)
        dirs = [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]

        total_edges = 0
        while queue:
            coord = queue.pop()
            edges = 0
            for d in dirs:
                new_coord = coord + d
                if new_coord in region_nodes:
                    edges += coords[new_coord] != region
                    continue
                if new_coord in coords and coords[new_coord] == region:
                    region_nodes.add(new_coord)
                    queue.appendleft(new_coord)
                    area += 1
                else:
                    edges += 1
            total_edges += edges

        visited |= region_nodes
        # perimeter = total_edges
        perimeter = part2(region_nodes)

        return (area, perimeter)

    def calc_price(area, perimeter):
        return area * perimeter

    total = 0
    for i, j in itertools.product(range(n), range(m)):
        coord = complex(i, j)
        if coord in visited:
            continue
        total += calc_price(*bfs(coord))

    return total


print(puzzle1())  # 1304764 and part 2 = 811148
