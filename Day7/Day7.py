with open("Day7.txt", "r") as file:
    test_values = []
    nums = []
    for line in file:
        line = line.split(":")
        test_values.append(int(line[0]))
        nums.append(list(map(int, line[1].split())))


def backtrack(val, numbers, index, total):
    if total == val and index == len(numbers):
        return True
    if index == len(numbers) or total > val:
        return False

    return (
        backtrack(val, numbers, index + 1, total + numbers[index])
        or backtrack(val, numbers, index + 1, total * numbers[index])
        or backtrack(val, numbers, index + 1, int(str(total) + str(numbers[index])))
    )


def puzzle1():
    """
    try all possible combinations + or *.
    if it can equal test value return the total
    """

    return sum(
        val if backtrack(val, numbers, 1, numbers[0]) else 0
        for val, numbers in zip(test_values, nums)
    )


print(puzzle1())
# Puzzle 1 = 2654749936343
# Puzzle 2 = 124060392153684
