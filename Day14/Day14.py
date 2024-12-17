import re

with open("Day14.txt", "r") as file:
    """
    101 wide
    103 tall
    coordinates are expressed as how far from left wall
    and how far from top wall
    """
    n, m = 103, 101
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    robots = []
    for line in file:
        robots.append(list(map(int, re.findall(r"-?\d+", line))))


def puzzle1(seconds=100):
    """
    find how many are in each quadrant after 100 seconds
    """
    for left, down, vleft, vdown in robots:
        matrix[(down + vdown * seconds) % n][(left + vleft * seconds) % m] += 1

    q1, q2, q3, q4 = [0] * 4
    for i in range(n // 2):
        for j in range(m // 2):
            q1 += matrix[i][j]
            q2 += matrix[i][m - j - 1]
            q3 += matrix[n - i - 1][j]
            q4 += matrix[n - i - 1][m - j - 1]

    return q1 * q2 * q3 * q4


def puzzle2():
    """
    Used the hueristic of having a diagonal line of size x.
    I chose a low x and had a lot of hits.
    When I changed x = 10 I got only the correct answer.
    """
    # for s in range(10000):
    for s in [math_puzzle2(x) for x in range(2)]:
        for left, down, vleft, vdown in robots:
            matrix[(down + vdown * s) % n][(left + vleft * s) % m] += 1

        # prune by looking for a diagonal
        tree = False
        x = 10
        for i in range(n - x):
            for j in range(m - x):
                y = x
                while matrix[i + y][j + y] > 0 and y:
                    y -= 1
                if y == 0:
                    print(i, j)
                    tree = True
                    break
            if tree:
                break

        if tree:
            for row in matrix:
                new_row = []
                for col in row:
                    new_row.append(" " if col == 0 else ".")
                print("".join(new_row))
                # print("".join(map(str, row)))
            print("_______________________", s, "_________________________________")

        for left, down, vleft, vdown in robots:
            matrix[(down + vdown * s) % n][(left + vleft * s) % m] -= 1


def math_puzzle2(x=0):
    """
    noticed that maps 14 and 94 look interesting.
    14 has many verticle lines.
    94 has many horizontal lines.
    103 tall so the horizontal lines would repeat after 103x + 94.
    101 wide so the vertical lines would repeat after 101x + 14.
    We can apply Chinesse Remainder Theorem to solve this to get the answer.
    (x mod 103 = 94) and (x mod 101 = 14)
    First check that the modulos are coprime.
    103 and 101 are coprime because gcd(101, 103) == 1.
    Because of Modular arithmetic and this rule.
    a = b mod m same as b = a mod m.
    so we have x = 94 mod 103 and x = 14 mod 101.
    The goal is to have mod 103 cancel out the other 14 mod 101, and vice versa.
    x = 101 mod 103 + 103 mod 101
    x = 101 mod 103 + 2 mod 101
    we want 94 mod 103 and 14 mod 101.
    Multiply the 103 by 7 and we get 721 mod 101 = 14 mod 101
    And Multiply 101 by 56 and we get 5656 mod 103 = 94 mod 103
    x = 101 * 56 mod 103 + 103 * 7 mod 101
    x = 5656 mod 103 + 721 mod 101
    x = 6377 mod 10403
    When both the vertical and horizontal line up is at 6377 + 10403x
    """
    return 6377 + 10403 * x


# print(puzzle1()) # 225943500
puzzle2()  # 6377
