import itertools
import re

# from functools import cache


def parse(s):
    pattern = r"\d+"
    return complex(*map(int, re.findall(pattern, s)))


with open("Day13.txt", "r") as file:
    machines = []
    while a := file.readline():
        b = file.readline()
        prize = file.readline()
        file.readline()

        machine = {
            "a": parse(a),
            "b": parse(b),
            "prize": parse(prize),
        }
        machines.append(machine)


def puzzle1():
    """
    Button A costs 3 tokens and Button B costs 1 token.
    Smallest number of tokens to get to the prize on the machine.

    """

    def greater(x, y):
        return x.imag > y.imag or x.real > y.real

    def is_possible(machine):
        """
        Should take no more than 100 of each
        """
        a, b, prize = machine.values()
        tokens = float("inf")

        for i, j in itertools.product(range(100), range(100)):
            if a * i + b * j == prize:
                tokens = min(tokens, 3 * i + j)
        return 0 if tokens == float("inf") else tokens

        """
        @cache
        def dp(location):
            if greater(location, prize):
                return float("inf")
            if location == prize:
                return 0
            take_a = 3 + dp(location + a)
            take_b = 1 + dp(location + b)
            return min(take_a, take_b)

        tokens = dp(0j)
        return 0 if tokens == float("inf") else tokens
        """

    return sum(is_possible(machine) for machine in machines)


def puzzle2():
    """
    Same as part 1 but we need to use math to solve.
    """

    def is_possible(machine):
        """
        refer to ![[Linear Algebra Recap]]
        a = ((prize_x * y2) - (prize_y * x2)) / ((x1 * y2) - (x2 * y1))
        b = ((prize_x * -y1) + (prize_y * x1)) / ((x1 * y2) - (x2 * y1))
        """
        button_a, button_b, prize = machine.values()
        prize += complex(10000000000000, 10000000000000)
        x1, y1, x2, y2, prize_x, prize_y = (
            button_a.real,
            button_a.imag,
            button_b.real,
            button_b.imag,
            prize.real,
            prize.imag,
        )
        a = ((prize_x * y2) - (prize_y * x2)) / ((x1 * y2) - (x2 * y1))
        b = ((prize_x * -y1) + (prize_y * x1)) / ((x1 * y2) - (x2 * y1))
        a, b = int(a), int(b)

        return 3 * a + b if a * button_a + b * button_b == prize else 0

    return sum(is_possible(machine) for machine in machines)


print(puzzle2())  # 25629 part 2 = 107487112929999
# Part 1
# 4.39 seconds with dp
# 430.95 milliseconds with iterative sol
# Part 2 runs in 328.52 milliseconds
