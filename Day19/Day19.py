from collections import defaultdict
from functools import cache

with open("Day19.txt", "r") as file:

    """
    Order the towels
    Each tower is striped
    white (w), blue (u), black (b), red (r), or green (g)
    Can't be reversed.
    Given the available towel patterns, unlimited with all of those.
    and a list of desired designs.
    Return how many patterns are possible

    """
    towel_patterns = list(file.readline().strip().split(", "))
    file.readline()
    desired_patterns = [line.strip() for line in file]


class TrieNode:
    def __init__(self):
        self.chars = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.chars[c]
        node.is_word = True

    def print_trie(self):
        print(self.root.chars)

    @cache
    def is_possible(self, word):
        node = self.root
        for i, c in enumerate(word):
            if c in node.chars:
                node = node.chars[c]
            else:
                return False
            if node.is_word and self.is_possible(word[i + 1 :]):
                # print(word[0 : i + 1], word[i + 1 :])
                return True

        return node.is_word

    def is_possible_part2(self, word):
        x = self.dfs(0, word, self.root)
        return x

    @cache
    def dfs(self, index, word, node):
        c = word[index]
        if index == len(word) - 1:
            if node.chars[c].is_word:
                return 1
            return 0
        skip, take = 0, 0
        if c in node.chars:
            skip = self.dfs(index + 1, word, node.chars[c])
            node = node.chars[c]
            if node.is_word:
                take = self.dfs(index + 1, word, self.root)
        return skip + take


def puzzle1():
    """
    Find how many patterns are possible
    """
    trie = Trie(towel_patterns)
    return sum(trie.is_possible(word) for word in desired_patterns)


def puzzle2():
    """
    Find how many ways to make each of the possible patterns
    """
    trie = Trie(towel_patterns)
    return sum(trie.is_possible_part2(word) for word in desired_patterns)


# print(puzzle1())  # 360
# print(puzzle2())  # 577474410989846
