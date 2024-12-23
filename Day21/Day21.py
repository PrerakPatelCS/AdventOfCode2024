import re
from functools import cache

with open("Day21.txt", "r") as file:
    data = [line.strip() for line in file]

number_pad = {
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "A": (3, 2),
    "": (3, 0),
}

directional_pad = {
    "^": (0, 1),
    "A": (0, 2),
    "": (0, 0),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def compute_complexity(code, length):
    """
    The number in the code * the length of the input needed
    """
    num = list(map(int, re.findall("\\d+", code)))[0]
    return length * num


@cache
def number_pad_button(a, b):
    """
    start at x1 y1 and end at x2 y2
    horizontal is left right
    vertical is up and down
    """
    x1, y1, x2, y2 = *number_pad[a], *number_pad[b]
    horizontal, vertical = y2 - y1, x2 - x1
    h_dir, v_dir = ">" if horizontal > 0 else "<", ("v" if vertical > 0 else "^")

    if vertical == 0:
        return (
            directional_pad_button("A", h_dir)
            + abs(horizontal)
            + directional_pad_button(h_dir, "A")
            + 1
        )
    if horizontal == 0:
        return (
            directional_pad_button("A", v_dir)
            + abs(vertical)
            + directional_pad_button(v_dir, "A")
            + 1
        )

    total = int(1e18)
    # check gap when going horizontal then vertical
    if (x1, y1 + horizontal) != number_pad[""]:
        total = min(
            total,
            (
                directional_pad_button("A", h_dir)
                + abs(horizontal)
                + directional_pad_button(h_dir, v_dir)
                + abs(vertical)
                + directional_pad_button(v_dir, "A")
                + 1
            ),
        )

    # check gap when going vertical then horizontal
    if (x1 + vertical, y1) != number_pad[""]:
        total = min(
            total,
            (
                directional_pad_button("A", v_dir)
                + abs(vertical)
                + directional_pad_button(v_dir, h_dir)
                + abs(horizontal)
                + directional_pad_button(h_dir, "A")
                + 1
            ),
        )

    return total


@cache
def directional_pad_button(dir1, dir2, chain=2):
    """
    Going to the direction costs manhattan distance.
    Going back to A costs manhattan distance.
    Clicking A for both direction and A costs 2.
    do both directions
    you want to go horizontal then vertical then A
    so finding the fastest path is important
    """
    x1, y1, x2, y2 = *directional_pad[dir1], *directional_pad[dir2]
    horizontal, vertical = y2 - y1, x2 - x1
    h_dir, v_dir = ">" if horizontal > 0 else "<", ("v" if vertical > 0 else "^")

    if chain == 1:
        return abs(x2 - x1) + abs(y2 - y1)

    if vertical == 0:
        return (
            directional_pad_button("A", h_dir, chain - 1)
            + abs(horizontal)
            + directional_pad_button(h_dir, "A", chain - 1)
        )
    if horizontal == 0:
        return (
            directional_pad_button("A", v_dir, chain - 1)
            + abs(vertical)
            + directional_pad_button(v_dir, "A", chain - 1)
        )

    total = int(1e18)
    # check gap when going horizontal then vertical
    if (x1, y1 + horizontal) != directional_pad[""]:
        total = min(
            total,
            (
                directional_pad_button("A", h_dir, chain - 1)
                + abs(horizontal)
                + directional_pad_button(h_dir, v_dir, chain - 1)
                + abs(vertical)
                + directional_pad_button(v_dir, "A", chain - 1)
            ),
        )

    # check gap when going vertical then horizontal
    if (x1 + vertical, y1) != directional_pad[""]:
        total = min(
            total,
            (
                directional_pad_button("A", v_dir, chain - 1)
                + abs(vertical)
                + directional_pad_button(v_dir, h_dir, chain - 1)
                + abs(horizontal)
                + directional_pad_button(h_dir, "A", chain - 1)
            ),
        )

    return total


def puzzle1():
    """
    Find how many operations we need to make the code
    through this chain of robots
    """
    sum_complexities = 0
    for x in data:
        prev = "A"
        total = 0
        for c in x:
            temp = number_pad_button(prev, c)
            total += number_pad_button(prev, c)
            prev = c
        sum_complexities += compute_complexity(x, total)
    return sum_complexities


print(puzzle1())
# Part 1 = 212488
# Part 2 = 258263972600402

"""
We have a robot that needs to input a password on this
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
We need to input moves onto this
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

1 numberpad
2 or 25 directional pads
a directional pad that I operate
"""
