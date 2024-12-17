from itertools import pairwise

with open("Day2.txt", "r") as file:
    """
    Each line is a report.
    A report is a list of numbers called levels.
    """
    reports = [[*map(int, line.split())] for line in file]


def is_safe(arr):
    """
    All inc or dec.
    Min diff is 1 and max is 3.
    """
    inc_dec = 1 if arr[0] > arr[1] else -1
    return all(
        (a > b if inc_dec == 1 else a < b) and abs(a - b) >= 1 and abs(a - b) <= 3
        for a, b in pairwise(arr)
    )


def puzzle1():
    """
    Find which reports are safe.
    """

    return sum(is_safe(report) for report in reports)


def puzzle2():
    """
    Find which reports are safe.
    Have 1 dampening, can remove 1 so it will be safe.
    """

    def is_safe_damp(arr):
        for i in range(len(arr)):
            new_arr = arr[0:i] + arr[i + 1 :]
            if is_safe(new_arr):
                return True
        return False

    return sum(is_safe_damp(report) for report in reports)


print(puzzle1())  # 686
print(puzzle2())  # 717
