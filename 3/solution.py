from typing import Dict
from operator import mul
from collections import defaultdict


def read_schematic(filename: str):
    with open(filename, "r") as f:
        schematic = [f".{line}." for line in f.read().splitlines()]
    empty_line = "." * len(schematic[0])
    schematic = [empty_line] + schematic + [empty_line]
    return schematic


def get_adjacent_symbols(schematic: list[str], y_center: int, x_start: int, x_end: int):
    adjacent_symbols = []
    for y in range(y_center - 1, y_center + 2):
        for x in range(x_start - 1, x_end + 2):
            char = schematic[y][x]
            if char != "." and not char.isdigit():
                adjacent_symbols.append((char, x, y))
    return adjacent_symbols


def get_all_symbols(filename: str):
    schematic = read_schematic(filename)
    symbols = defaultdict(list)
    for y, row in enumerate(schematic):
        x_start = None
        for x, char in enumerate(row):
            if char.isdigit():
                if x_start is None:
                    x_start = x
            elif x_start is not None:
                for identifier in get_adjacent_symbols(schematic, y, x_start, x - 1):
                    number = int(row[x_start:x])
                    symbols[identifier].append(number)
                x_start = None
    return symbols


def solve_1(symbols: Dict[str, list[int]]):
    return sum([sum(numbers) for numbers in symbols.values()])


def solve_2(symbols: Dict[str, list[int]]):
    result = 0
    for (char, x, y), numbers in symbols.items():
        if char == "*" and len(numbers) > 1:
            result += mul(*numbers)
    return result


def solve(filename: str):
    print(filename)
    symbols = get_all_symbols(filename)

    print(" part 1:", solve_1(symbols))
    print(" part 2:", solve_2(symbols))


solve("example.txt")  # 4361, 467835
solve("input.txt")  # 525911, 75805607
