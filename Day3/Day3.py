with open("Day3.txt", "r") as file:
    input = "".join(line for line in file)


def puzzle1():
    n, i, total = len(input), 0, 0
    while i <= n - 4:
        if input[i : i + 4] == "mul(":
            j = i + 4 + 1
            while input[j] in "1234567890,":
                j += 1
            is_valid = input[j] == ")" and "," in input[i : j + 1]
            if is_valid:
                nums = list(map(int, input[i + 4 : j].split(",")))
                total += nums[0] * nums[1]
            i = j
        i += 1

    return total


def puzzle2():
    n, i, total = len(input), 0, 0
    enabled = True
    while i <= n - 4:
        if i <= n - 7 and input[i : i + 7] == "don't()":
            enabled = False
        else if i <= n - 4 and input[i : i + 4] == "do()":
            enabled = True
        else if input[i : i + 4] == "mul(":
            j = i + 4 + 1
            while input[j] in "1234567890,":
                j += 1
            is_valid = input[j] == ")" and "," in input[i : j + 1]
            if is_valid and enabled:
                nums = list(map(int, input[i + 4 : j].split(",")))
                total += nums[0] * nums[1]
            i = j
        i += 1

    return total


print(puzzle2())
