import time
from collections import Counter
from functools import cache

with open("Day11.txt", "r") as file:
    data = Counter(map(int, file.read().strip().split()))


def puzzle1(stones, rounds=75):
    """
    Number and the length of the number matter but the position doesn't.
    We will have many repeat numbers so we can use a frequency map.
    """

    @cache
    def new_stone(stone):
        ans = []
        if stone == 0:
            ans.append(1)
        elif len(str(stone)) % 2 == 0:
            string_stone = str(stone)
            mid = len(string_stone) // 2
            left, right = string_stone[:mid], string_stone[mid:]
            ans += map(int, [left, right])
        else:
            ans.append(stone * 2024)
        return ans

    for _ in range(rounds):
        new_stones = Counter()
        for stone, count in stones.items():
            for num in new_stone(stone):
                new_stones[num] += count
        stones = new_stones

    return sum(stones.values())


start_time = time.time()
print(puzzle1(data))  # 183484 and puzzle2 218817038947400
end_time = time.time()
print(
    "TIME = ", end_time - start_time
)  # .13 seconds with no cache, .06 seconds with cache
