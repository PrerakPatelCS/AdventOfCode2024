from collections import Counter

with open("Day22.txt", "r") as file:
    data = list(map(int, file))


def get_next(x):
    MOD = 16777216
    x = ((x * 64) ^ x) % MOD
    x = ((x // 32) ^ x) % MOD
    x = ((x * 2048) ^ x) % MOD
    return x


def puzzle1():
    """
    Multiply by 64, then XOR by prev number and mod 16777216
    Divide by 32 and do that.
    Multiply by 2048.
    """
    total = 0
    for x in data:
        for _ in range(2000):
            x = get_next(x)
        total += x
    return total


def puzzle2():
    """
    The price is actually the ones digit from each secret number.
    A monkey is in charge of how you sell.
    It looks at 4 consecutive changes in price then immediately sells.
    Go through every price difference, A sequence of 4.
    Make every sequence of 4 and then try it out
    """

    sequences = Counter()
    for num in data:
        new_sequences = Counter()
        for count in range(2000):
            match count:
                case 0:
                    prev1 = num % 10
                    num = get_next(num)
                case 1:
                    prev2 = num % 10
                    num = get_next(num)
                case 2:
                    prev3 = num % 10
                    num = get_next(num)
                case 3:
                    prev4 = num % 10
                    num = get_next(num)
                case _:
                    diff1, diff2, diff3, diff4 = (
                        prev1 - prev2,
                        prev2 - prev3,
                        prev3 - prev4,
                        prev4 - num % 10,
                    )
                    seq = (diff1, diff2, diff3, diff4)
                    if seq not in new_sequences:
                        new_sequences[seq] = num % 10
                    prev1, prev2, prev3, prev4 = prev2, prev3, prev4, num % 10
                    num = get_next(num)
        sequences += new_sequences

    return max(sequences.values())


print(puzzle1())  # 16999668565
print(puzzle2())  # 1898
