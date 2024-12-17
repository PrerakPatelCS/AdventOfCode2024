with open("Day9.txt", "r") as file:
    disk_map = list(int(x) for x in file.readline().strip())


def make_blocks():
    ans = []
    count = 0
    for left, num in enumerate(disk_map):
        if not left & 1:
            ans += [count] * num
            count += 1
        else:
            ans += "." * num
    return ans


def puzzle1():

    blocks = make_blocks()
    n = len(blocks)
    left, right = 0, n - 1

    while left <= right:
        if blocks[left] == ".":
            blocks[left], blocks[right] = blocks[right], blocks[left]
            right -= 1
            while blocks[right] == ".":
                right -= 1
        left += 1
    return sum(i * num for i, num in enumerate(map(int, blocks[:left])))


def make_blocks2():
    ans = []
    count = 0
    for left, num in enumerate(map(int, disk_map)):
        if not left & 1:
            ans.append((count, num))
            count += 1
        else:
            ans.append((-1, num))
    return ans


def puzzle2():
    blocks = make_blocks2()
    left = 0

    def expand(blocks):
        ans = []
        for num, count in blocks:
            ans += [num] * count
        # print("".join(map(str, ans)))
        return ans

    while left < len(blocks):
        num, count = blocks[left]
        if num == -1:
            right = len(blocks) - 1
            while right > left and (blocks[right][1] > count or blocks[right][0] <= 0):
                right -= 1
            num2, count2 = blocks[right]
            blocks[right] = (0, count2)
            if count == count2:
                blocks[left] = (num2, count2)
            else:
                blocks[left] = (num2, count2)
                blocks.insert(left + 1, (num, count - count2))

        left += 1

    return sum(i * num if num > 0 else 0 for i, num in enumerate(expand(blocks)))


# print(puzzle1())  # 6330095022244
print(puzzle2())  # 6359491814941
