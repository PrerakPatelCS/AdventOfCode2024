from collections import defaultdict

with open("Day5.txt", "r") as file:
    rules, updates = [], []
    for line in file:
        if "|" in line:
            rules.append(list(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))


def puzzle1():
    """
    rules are that X|Y X must be before Y in an update.
    An update is valid is the rule for
    a b c d e
    c | a does not exist and all those combinations.
    for each number we make a list of what the rules say it has to be before.
    """
    before = defaultdict(set)
    for a, b in rules:
        before[a].add(b)

    total = 0
    for update in updates:
        valid = True
        for i, a in enumerate(update):
            for j in range(i):
                b = update[j]
                if b in before[a]:
                    valid = False
                    break

        if valid:
            total += update[len(update) // 2]

    return total


def puzzle2():
    """
    Fix the wrong updates.
    Find how many rules each number has that are in the rules.
    Based on the rules make the correct update.
    """

    def fix(update):
        counts = defaultdict(int)
        for num1 in update:
            for num2 in update:
                if num1 == num2:
                    continue
                elif num2 in before[num1]:
                    counts[num1] += 1

        return sorted(update, key=lambda x: counts[x])

    before = defaultdict(set)
    for a, b in rules:
        before[a].add(b)

    total = 0
    for update in updates:
        valid = True
        for i, a in enumerate(update):
            for j in range(i):
                b = update[j]
                if b in before[a]:
                    valid = False
                    break

        if not valid:
            total += fix(update)[len(update) // 2]

    return total


# print(puzzle1())  # 5374
print(puzzle2())  #
