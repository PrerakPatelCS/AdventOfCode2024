from collections import Counter

left_list, right_list = [], []
with open("Day1.txt", "r") as file:
    for line in file:
        a, b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))


def puzzle1():
    """
    given 2 lists pair up the smallest in the left and the right lists.
    Figure out how far apart they are.
    Add up all those distances.
    """
    return sum(abs(a - b) for a, b in zip(sorted(left_list), sorted(right_list)))


def puzzle2():
    """
    Find how many times a number in the left list appears in the right list.
    Calculate the total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
    """
    freq = Counter(right_list)
    return sum(num * freq[num] for num in left_list)


print(puzzle2())
# Puzzle 1 = 1722302
# Puzzle 2 = 20373490
